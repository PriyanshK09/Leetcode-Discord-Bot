import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.command()
async def leetcode(ctx, *, problem_name):
    try:
        # Create a session to maintain cookies
        session = requests.Session()

        # Fetch the LeetCode problem and its solution
        url = f'https://leetcode.com/problems/{problem_name}/description/?envType=daily-question&envId=2024-02-27'
        print(f"Fetching URL: {url}")
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        problem_title_element = soup.find('h4', class_='content__title')
        if problem_title_element is None:
            raise Exception(f"Problem '{problem_name}' not found")

        problem_title = problem_title_element.text
        problem_solution_element = soup.find('div', class_='content__u3I1 question-content__JfgR').find('div')
        if problem_solution_element is None:
            raise Exception("Solution not found")
        problem_solution = problem_solution_element.text

        # Send the solution to a certain channel
        channel_id = 1101818536646688799
        channel = bot.get_channel(channel_id)
        await channel.send(f"{problem_title}\n\nSolution for {problem_title}:\n{problem_solution}")

        # Ping a certain role
        role_id = 1211196331419246622
        role = ctx.guild.get_role(role_id)
        await ctx.send(f"Solution sent to {channel.mention}! {role.mention}")

    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"An error occurred: {e}")


bot.run('TOKEN')

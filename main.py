import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.command()
async def leetcode(ctx, *, problem_name_lang):
    try:
        problem_name, lang = problem_name_lang.split()
        lang = lang.lower()
        # Create a session to maintain cookies
        session = requests.Session()

        # Fetch the LeetCode problem and its solution
        url = f'https://leetcode.com/problems/{problem_name}/description/'
        print(f"Fetching URL: {url}")
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        problem_title_element = soup.find('title')
        if problem_title_element is None:
            raise Exception(f"Problem '{problem_name}' not found")

        problem_title = problem_title_element.text.strip()
        problem_description_element = soup.find('meta', attrs={'name': 'description'})
        if problem_description_element is None:
            raise Exception("Description not found")
        problem_description = problem_description_element['content']

        # Create an embed for the question
        embed = discord.Embed(title=problem_title, description=problem_description, color=0x00ff00)
        await ctx.send(embed=embed)

        # Find the solution file in the bot's directory
        solution_folder = os.path.join(os.getcwd(), 'solutions')
        if not os.path.exists(solution_folder):
            os.makedirs(solution_folder)
        solution_file = os.path.join(solution_folder, f'{problem_name}.{lang}')

        # Read the solution from the file
        with open(solution_file, 'r') as f:
            problem_solution = f.read()

        # Send the solution in an embed
        embed_solution = discord.Embed(title=f"Solution for {problem_title}", description=problem_solution, color=0x00ff00)
        await ctx.send(embed=embed_solution)

    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"An error occurred: {e}")


bot.run('TOKEN')

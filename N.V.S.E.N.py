import discord
import random
from discord.ext import commands
import discord.types
import time

description = '''N.V.S.E.N Es un bot desarollado para dar una nueva perspectiva mas objetiva sobre la energia nuclear'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = '#', description = description, intents = intents)

links_estudios = [
    'https://energy.mit.edu/area/nuclear/',
    'https://ourworldindata.org/safest-sources-of-energy',
    'https://www.nrel.gov/news/program/2020/nuclear-renewable-synergies-for-clean-energy-solutions.html',
    'https://www.iaea.org/newscenter/news/what-is-nuclear-energy-the-science-of-nuclear-power#:~:text=Nuclear%20energy%20is%20a%20form,fusion%20–%20when%20nuclei%20fuse%20together.'
    "https://www.iaea.org/newscenter/news/what-is-nuclear-fusion"
    "https://www.csn.es/fusion-nuclear"

]
links_videos = [
    'https://www.youtube.com/watch?v=J3znG6_vla0',
    'https://www.youtube.com/watch?v=glM80kRWbes',
    'https://www.youtube.com/watch?v=IzQ3gFRj0Bc'
    'https://www.youtube.com/watch?v=lL6uB1z95gA&t=909s'

]

@bot.event
async def on_ready():
    print(f'Logged as: {bot.user} (ID: {bot.user.id}) ')


@bot.command(name='com')
async def com(ctx):
    embed = discord.Embed(
        title="Comandos",
        description="Estos son los comandos disponibles",
        color=discord.Color.green()
    )
    embed.add_field(name="#com", value="Muestra los comandos del bot", inline=False)
    embed.add_field(name="#info_v", value="Da un link a un video sumamente detallado sobre la energia nuclear", inline=False)
    embed.add_field(name="#info", value="Da una lsita de links a estudios sobre la energia nuclear o estudios relacionado con ella", inline=False)
    embed.add_field(name="#video_al", value="Da un link a un video aleatorio sobre la energia nuclear ", inline=False)
    embed.add_field(name="#info_al", value="Da un link a un video aleatorio sobre la energia nuclear ", inline=False)
    embed.add_field(name="#video", value="Da una lsita de videos sobre la energia nuclear ", inline=False)
    embed.add_field(name="#cuest", value="Hace un cuestionario sobre los conocimientos basicos sobre la energía nuclear", inline=False)
    embed.add_field(name="#_NVSEN_", value="Proporciona una descripcíon y el proposito del bot", inline=False)

    await ctx.send(embed=embed)


@bot.command(name='info_v')
async def info_v(ctx):
    slideshow_url = 'https://www.youtube.com/watch?v=yMmB36Nxvy8'
    embed = discord.Embed(
        title="Video Informatico",
        description="Link a video informatico sobre la enegia nuclear:",
        color=discord.Color.dark_blue()
    )
    embed.add_field(name="", value=f"[Desmontando mentiras ecologistas sobre la energía nuclear]({slideshow_url})", inline=False)
    await ctx.send(embed=embed)


@bot.command(name='info_al')
async def info_al(ctx):
    slideshow_url = random.choice(links_estudios)
    embed = discord.Embed(
        title="Pagina Informatica",
        description="Link de un estudio aleatoreo sobre la energia nuclear:",
        color=discord.Color.purple()
    )
    embed.add_field(name="", value=f"[NUCLEAR ENERGY]({slideshow_url})", inline=False)
    await ctx.send(embed=embed)


@bot.command(name='video_al')
async def video_al(ctx):
    slideshow_url = random.choice(links_videos)
    embed = discord.Embed(
        title="Un video aleatorio",
        description="Un video aleatorio sobre la energia nuclear",
        color=discord.Color.blue()
    )
    embed.add_field(name="Video", value=f"[NUCLEAR]({slideshow_url})", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='info')
async def info(ctx):
    lnk1 = 'https://energy.mit.edu/area/nuclear/'
    lnk2 = 'https://ourworldindata.org/safest-sources-of-energy'
    lnk3 = 'https://www.nrel.gov/news/program/2020/nuclear-renewable-synergies-for-clean-energy-solutions.html'
    lnk4 = 'https://www.iaea.org/newscenter/news/what-is-nuclear-energy-the-science-of-nuclear-power#:~:text=Nuclear%20energy%20is%20a%20form,fusion%20–%20when%20nuclei%20fuse%20together'
    lnk5 = 'https://www.iaea.org/newscenter/news/what-is-nuclear-fusion'
    lnk6 = 'https://www.csn.es/fusion-nuclear'
    embed = discord.Embed(
        title="Paginas Informaticas",
        description="Lista de estudios sobre la energia nuclear:",
        color=discord.Color.purple()
    )
    embed.add_field(name="", value=f"[MIT Nuclear Initiative]({lnk1})", inline=False)
    embed.add_field(name="", value=f"[What are the safest and cleanest sources of energy?]({lnk2})", inline=False)
    embed.add_field(name="", value=f"[Nuclear–Renewable Synergies for Clean Energy Solutions]({lnk3})", inline=False)
    embed.add_field(name="", value=f"[What is Nuclear Energy? The Science of Nuclear Power]({lnk4})", inline=False)
    embed.add_field(name="", value=f"[What is Nuclear Fusion?]({lnk5})", inline=False)
    embed.add_field(name="", value=f"[Fusión nuclear]({lnk6})", inline=False)

    await ctx.send(embed=embed)

@bot.command(name='video')
async def video(ctx):
    vid1 = 'https://www.youtube.com/watch?v=J3znG6_vla0'
    vid2 = 'https://www.youtube.com/watch?v=glM80kRWbes'
    vid3 = 'https://www.youtube.com/watch?v=IzQ3gFRj0Bc'
    vid4 = 'https://www.youtube.com/watch?v=lL6uB1z95gA&t=909s'
    embed = discord.Embed(
        title="Paginas Informaticas",
        description="Lista de videos sobre la energia nuclear:",
        color=discord.Color.blue()
    )
    embed.add_field(name="", value=f"[Why You’re Wrong About Nuclear Power]({vid1})", inline=False)
    embed.add_field(name="", value=f"[The Truth About Nuclear Energy]({vid2})", inline=False)
    embed.add_field(name="", value=f"[Nuclear–Renewable Synergies for Clean Energy Solutions]({vid3})", inline=False)
    embed.add_field(name="", value=f"[Renewable Energy is The Scam We All Fell For]({vid4})", inline=False)

    await ctx.send(embed=embed)

@bot.command(name='_NVSEN_')
async def _NVSEN_(ctx):    
    await ctx.send(f"Hola! soy N.V.S.E.N mi funcionalidad principal es difundir informacion sobre la energia nuclear pero mas alla de eso mi acronimo señala mi principal objetivo ya que este significa:\n\nN: Nueva\n\nV: Vision\n\n S: Sobre la\n\nE: Energia\n\nN: Nuclear\n\nComo este indica mi objetivo principal es proporcionar una vision mas realista y objetiva sobre la energia nuclear ")
    await ctx.send(f"Bajo estos objetivos, estoy a sus ordenes")
    await ctx.send(file = discord.File('NVSEN.webp'))

@bot.command(pass_context=True)
async def cuest(ctx):    
    await ctx.send(f"¡Hola! Bienvenido/a al cuestionario sobre la energía nuclear. Tu participación es esencial para conocer las opiniones y conocimientos que tienes sobre este tema. No necesitas ser un experto; queremos conocer tus perspectivas sinceras. Para iniciar escribe -Iniciar- si no estas listo ignora este mensaje o escribe -Cancelar-.")
    await ctx.send(file = discord.File('image.png'))
    def check(a):
        return a.author == ctx.author and a.content in ["Iniciar", "Cancelar"]
    try:
        inicio = await bot.wait_for('message', check=check, timeout = 30)
        if inicio.content == "Iniciar":
            await ctx.send(f"Perfecto has decidido iniciar el cuestionario. Comencemos!")
        elif inicio.content == "Cancelar":
            await ctx.send(f"Has decidido cancelar! ¿Te puedo ayudar con otra cosa?")
            await ctx.send(f"")
        else:
            await ctx.send(f"")
        KP = 5

        #---------------- 
        await ctx.send(f"¿Que es la energia nuclear?\nA) La energía nuclear es una forma de energía renovable que se produce exclusivamente a partir de fuentes naturales como el viento y el agua \n\nB) a energía nuclear se genera quemando materiales radiactivos como el carbón y el petróleo en reactores especiales \n\nC) La energía nuclear se genera a través de reacciones nucleares, como la fisión del núcleo de átomos pesados como el uranio, liberando grandes cantidades de energía en forma de calor.")
        
        def check_q(q1):
            return q1.author == ctx.author and q1.content in ["A", "B", "C"]
        q1r = await bot.wait_for('message', check=check_q, timeout = 60)

       
        if q1r.content.upper() == "C":
            await ctx.send(f"Respuesta recibida")
            KP += 1
            time.sleep(1)
        elif q1r.content.upper() == "A":
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
        else:
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)

        #---------------- 
        await ctx.send(f"¿En la siguente imagen el humo que sale de las chimeneas de la palnta nuclear es?")
        await ctx.send(file = discord.File('image (1).png'))
        await ctx.send(f"A) Vapor de agua\n\nB) Dioxido de Carbono\n\nC) Residuos Radioactivos")

        def check_q(q1):
            return q1.author == ctx.author and q1.content in ["A", "B", "C"]
        q1r = await bot.wait_for('message', check=check_q, timeout = 30)

       
        if q1r.content.upper() == "A":
            await ctx.send(f"Respuesta recibida")
            KP += 1
            time.sleep(1)
        elif q1r.content.upper() == "B":
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
        else:
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
            
        #---------------- 
        await ctx.send(f"¿Qué tipo de reacción nuclear se utiliza en las plantas de energía nuclear?")
        await ctx.send(file = discord.File('atom_noun_004_0115.jpg'))
        await ctx.send(f"A) Oxidación\n\nB) Dioxido de Combustión\n\nC) Fisión")

        def check_q(q1):
            return q1.author == ctx.author and q1.content in ["A", "B", "C"]
        q1r = await bot.wait_for('message', check=check_q, timeout = 30)

       
        if q1r.content.upper() == "C":
            await ctx.send(f"Respuesta recibida")
            KP += 1
            time.sleep(1)
        elif q1r.content.upper() == "A":
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
        else:
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
            
        #---------------- 
        await ctx.send(f"¿Cual es la taza de mortalidad de la energia nuclear incluyendo los accidentes de Chernobyl y Fukushima?")
        await ctx.send(file = discord.File('kilian-karger-ctklczb9hea-unsplash_1.jpg'))
        await ctx.send(f"A) 2.8 Muertes por teravatio-hora\n\nB) 0.3 Muertes por teravatio-hora\n\nC) 24.6 Muertes por teravatio-hora")

        def check_q(q1):
            return q1.author == ctx.author and q1.content in ["A", "B"]
        q1r = await bot.wait_for('message', check=check_q, timeout = 30)

       
        if q1r.content.upper() == "B":
            await ctx.send(f"Respuesta recibida")
            KP += 1
            time.sleep(1)
        elif q1r.content.upper() == "C":
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
        else:
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
        #---------------- 
        await ctx.send(f"¿La energía nuclear es una fuente de enrgia limpia?")
        await ctx.send(file = discord.File('news-jisea-istock-510637684.jpg'))
        await ctx.send(f"A) Si\n\nB) No")

        def check_q(q1):
            return q1.author == ctx.author and q1.content in ["A", "B"]
        q1r = await bot.wait_for('message', check=check_q, timeout = 30)

       
        if q1r.content.upper() == "A":
            await ctx.send(f"Respuesta recibida")
            KP += 1
            time.sleep(1)
        else:
            await ctx.send(f"Respuesta recibida")
            KP -= 1
            time.sleep(1)
        
        #---------------- 
        if KP > 8 :
            await ctx.send(f"Tus conocimentos sobre la energia nuclear son avanzados")
        elif KP > 5 and KP < 7:
            await ctx.send(f"Tus conocimentos sobre la energia nuclear son decentes")
        else:
            await ctx.send(f"Tus conocimentos sobre la energia nuclear bajos")

        #----------------
        async def Res(ctx):
            embed = discord.Embed(
                title="Resultados",
                description="Estos son los resultados correctos del cuestionario",
                color=discord.Color.green()
            )
            embed.add_field(name="Pregunta 1", value="C", inline=False)
            embed.add_field(name="Pregunta 2", value="A", inline=False)
            embed.add_field(name="Pregunta 3", value="C", inline=False)
            embed.add_field(name="Pregunta 4", value="B", inline=False)
            embed.add_field(name="Pregunta 5", value="A", inline=False)
            await ctx.send(embed=embed)
            await ctx.send(Res)
            await ctx.send(embed)
    except:
        await ctx.send(f"")

bot.run("MTMxMjQ4NzIwNTA3NTI4ODI4NA.GNO834.wdFKGbYwixwrLGKUQoQy2yFbLFxCZOPHZp-8cI")
import discord
from discord.ext import commands
from datetime import datetime



def is_leak_miladi(year):
    if year % 400 == 0:
        return True
       
    elif year % 100 == 0:
        return True

    elif year % 4 == 0:
        return True
    else:  
        return False
    
def next_year_miladi(day, month,year):
    return 1,1, year +1

def next_month_miladi(day,month,year):
    if month != 12:
        return 1,month+1,year
    else:
        return next_year_miladi(day,month,year)
    
def next_day_miladi(day,month,year):
    if is_leak_miladi(year):
        days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]              
    if day == days_in_month[month -1]:
        return next_month_miladi(day,month,year)
    else:
        return day+1,month,year         

def miladi_to_day(last_day, last_month, last_year):
    day_counter = 0
    start_day = 1
    start_month = 1
    start_year = 1
    while True:
        if start_day == last_day and start_month == last_month and start_year == last_year:
            break
        day_counter += 1
        start_day, start_month, start_year = next_day_miladi(start_day, start_month, start_year)
    return day_counter

def day_to_miladi(days):
    start_day = 1
    start_month = 1
    start_year = 1
    while True:
        if days == 0:
            break
        days-=1
        start_day, start_month, start_year = next_day_miladi(start_day, start_month, start_year)
    return start_day, start_month, start_year



def is_leak_hicri(year):
    if year % 30 == 2 or year % 30 == 5 or year % 30 == 7 or year % 30 == 10 or year % 30 == 13 or year % 30 == 15 or year % 30 == 18 or year % 30 == 21 or year % 30 == 24 or year % 30 == 24 or year % 30 == 26 or year % 30 == 25:
        return True
    else:  
        return False
    
def next_year_hicri(day, month,year):
    return 1,1, year +1

def next_month_hicri(day,month,year):
    if month != 12:
        return 1,month+1,year
    else:
        return next_year_hicri(day,month,year)
    
def next_day_hicri(day,month,year):
    if is_leak_hicri(year):
        days_in_month = [30,29,30,29,30,29,30,29,30,29,30,30]
    else:
         days_in_month = [30,29,30,29,30,29,30,29,30,29,30,29]              
    if day == days_in_month[month -1]:
        return next_month_hicri(day,month,year)
    else:
        return day+1,month,year         

def hicri_to_day(last_day, last_month, last_year):
    day_counter = 0
    start_day = 1
    start_month = 1
    start_year = 1
    while True:
        if start_day == last_day and start_month == last_month and start_year == last_year:
            break
        day_counter += 1
        start_day, start_month, start_year = next_day_hicri(start_day, start_month, start_year)
    return day_counter

def day_to_hicri(days):
    start_day = 1
    start_month = 1
    start_year = 1
    while True:
        if days == 0:
            break
        days-=1
        start_day, start_month, start_year = next_day_hicri(start_day, start_month, start_year)
    return start_day, start_month, start_year

def miladi_to_hicri(day, month, year):
    day1 = hicri_to_day(23,12,1444)
    day2 = miladi_to_day(11,7,2023)
    delta_day = day2-day1
    days = miladi_to_day(day,month,year)
    return day_to_hicri(days- delta_day)



bot = commands.Bot(command_prefix= "₺" , intents = discord.Intents.all())
"""
@bot.command(name="99")
async def nine_nine(ctx):
    a = "Selam Gardaş Nassın"
    await ctx.author.send(a)
@bot.event
async def member_join(member):
    if not member.bot:
        channel = member.get_channel("channel_id")
        await channel.send("insert message")
"""
global kanal_belirle

@bot.command(name="kanalBelirle")
@commands.has_role("👑Kurucu")
async def kanal_belirle(member):
    kanal = member.channel
    kanal_adi = str(kanal)
    await kanal.send("Belirlenilmiş kanal " + kanal_adi + " olarak değiştirildi")

@bot.command(name="miladi")
async def miladiGun(member):
    kanal = member.channel
    tarih = datetime.now()
    tarih_str = str(tarih.day)+"/"+str(tarih.month)+"/"+str(tarih.year)
    await kanal.send(tarih_str)

@bot.command(name="hicri")
async def hicriGun(member):
    kanal = member.channel
    tarih = datetime.now()

    day,month,year= miladi_to_hicri(tarih.day,tarih.month,tarih.year)
    tarih_str = str(day)+"/"+str(month)+"/"+str(year)
    await kanal.send(tarih_str)


if __name__ == "__main__":
    bot.run("MTEyNzk3MDM3OTk3ODI1NjQ5NQ.Gcx7dq.9kaZ6RwvGks8BERj_EeS1KQTZ4iVVYzlnJqbw0")
    



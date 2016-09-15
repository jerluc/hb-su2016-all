import films


def main():
    while True:
        films.movies()
        films.find_movies()
        string = raw_input('Do you want to continue?')
        if string != 'yes':
            break


if __name__ == "__main__":
    main()

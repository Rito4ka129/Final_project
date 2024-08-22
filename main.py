import final_project


def main():
    while True:
        print('Select a menu item:\n1 Top Queries:\n2 search for a movie by actor:'
              '\n3 search for a movie by title:\n4 search for a movie by year:\n5 search for a movie by description:'
              '\n6 search for a movie by category:\n7 search for a movie by keyword:')
        search_param = input('Your search parameter or "Top Result": ').lower()
        if search_param == '1':
            final_project.get_top_result()
        elif search_param == '2':
            actor_name = input('Enter actor name: ')
            final_project.print_result_actor(final_project.get_result_actor(actor_name))
        elif search_param == '3':
            title = input('Enter film title: ')
            final_project.print_result(final_project.get_result_title(title))
        elif search_param == '4':
            year = int(input('Enter year film: '))
            final_project.print_result(final_project.get_result_year(year))
        elif search_param == '5':
            description = input('Enter film description: ')
            final_project.print_result(final_project.get_result_description(description))
        elif search_param == '6':
            category = input('Enter film category: ')
            final_project.print_result(final_project.get_result_category(category))
        elif search_param == '7':
            try:
                keyword = input('Enter film keyword: ')
                final_project.print_result(final_project.get_result_keyword(keyword))
            except TypeError:
                print()


if __name__ == "__main__":
    main()



import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_status_code(language):
    '''status code is 200 if api call is successful'''
    # Make an API(Application Programming Interface) call and store the reponse
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    r = requests.get(url)

    return r.status_code

def most_starred_project(language):
    '''
    this function takes language name as parameter
    then get the most starred projects for that language on github
    '''

    # Make an API(Application Programming Interface) call and store the reponse
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    r = requests.get(url)
    print(f'Status code: {r.status_code}') #status_code = 200 if call was successful

    # Store API reponse in a variable
    response_dict = r.json() # converts the response in JSON format to a dictionary
    print(f'Total repositories: {response_dict["total_count"]}')

    # Explore info about the repositories
    repo_dicts = response_dict['items']
    print(f'Repositories returned: {len(repo_dicts)}')

    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        # build project name list
        names.append(repo_dict['name'])

        # build dict for each project
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': str(repo_dict['description']),
            'xlink': repo_dict['html_url'],
            }
        # append each dict to the list. To be used to create a tooltip for each project
        plot_dicts.append(plot_dict)

    # make visualization
    my_style = LS('#336', base_style=LCS)
    #
    # create configuration
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18 # y-axis label that mark increments of 5000
    my_config.truncate_label = 15 # truncate longer names than 15
    my_config.show_y_guides = False # hides horizontal lines
    my_config.width = 1000
    #
    # chart instance & settings
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = f'Most-Starred {language} on Github'
    chart.x_labels = names

    chart.add('', plot_dicts)

    chart.render_to_file(f'{language}_repos.svg')

# list of languages to work with
languages = ['javascript', 'ruby', 'c', 'java', 'perl', 'haskell', 'go', 'c#', 'c++']
count = 1
for language in languages:
    print(f' {count}: {language}')
    most_starred_project(language)
    print(f'completed with {language}!!!!!!!!')
    count += 1

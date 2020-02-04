"""Functions: Task 4"""


def path_wrapper(xml_str):
    """Main function"""
    path_list = xml_str.split(sep='>')  # Making a list
    del path_list[-1]  # Empty line at the end
    print('{\n\t\'name\': \'' + path_list[0][1:] + '\'', end='')
    dep = [1]  # Depth for tabs
    if len(path_list) > 2:
        print(',\n' + '\t'*dep[0] + '\'children\': [')
        dep[0] += 1
        for elem in path_list[1:-1]:
            if elem[-1] == '/':  # No children
                print('\t'*dep[0] + '{' + '\'name\': \''
                      + elem[1:-2] + '\',', end='')
                print('\'children\': []},')
            elif elem[1] == '/':  # Closing tag
                dep[0] -= 1
                print('\t'*dep[0] + ']')
                dep[0] -= 1
                print('\t'*dep[0] + '}')
            else:  # Node have children
                print('\t'*dep[0] + '{\n')
                dep[0] += 1
                print('\t'*dep[0] + '\'name\': \'' + elem[1:] + '\',')
                print('\t'*dep[0] + '\'children\': [')
                dep[0] += 1
        dep[0] -= 1  # Closing for root children
        print('\t'*dep[0] + ']')
    depth = 0
    for elem in path_list:  # Counting depth
        if elem[-1] != '/' and elem[1] != '/':
            depth += 1
    print('}, ' + str(depth))

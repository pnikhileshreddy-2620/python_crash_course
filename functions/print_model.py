def print_model(design,completed):

    while design:
        completed_desgin = design.pop(0)
        completed.append(completed_desgin)
        
    return completed
def show_completed_model(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)



unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

show_completed_model(print_model(unprinted_designs,[]))
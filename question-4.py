phone_models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Initial list of dictionaries : {}".format(models))
sorted_models = sorted(phone_models, key = lambda x: x['color'])
print("\nSorting the dictionaries : {}".format(sorted_models))

import sys
import expirements
from expirements import *
circuitID = 1
epochs = 20
ds_list=['1a','2a','3c']
#selected learning rates
lr_opt=[2.89,0.36,3.24]
model_list=[]
for i in range(3):
    data = load_data(ds_list[i])

    # Generate the splittings
    train_X, train_y, validate_X, validate_y, test_X, test_y = generate_train_validate_test_data(data)

    # Make the feature map
    feature_map= make_embedding_circuit()

    # Make the classifier
    ansatz = make_classifer_circuit(circuitID)

    # Do the training
    model = train_model(feature_map, ansatz, epochs, lr_opt[i], train_X, train_y)
    
    model_list.append(model)
    # Check the validation accuracy.
    val_accuracy = check_accuracy(model, test_X, test_y)
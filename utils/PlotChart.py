import matplotlib.pyplot as plt

def plot_chart(values, labels):
    # Create a bar chart
    plt.figure(figsize=(10, 6))

    plt.bar(labels, values)

    # Add labels to the axes
    plt.xlabel('Models')
    plt.ylabel('Accuracy')

    # Add a title to the chart
    plt.title('Test Accuracy')

    # Add values above the bars
    for i, value in enumerate(values):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')

    # Add specific labels for each point on the x-axis
    plt.xticks(range(len(labels)), labels)

    # Display the chart
    plt.show()

# Example of usage
values_list = [86.49, 89.19, 91.89, 72.97, 81.08, 75.68, 64.86]
names_of_values = ['EfficientNET', 'ConvNeXt', 'DenseNET', 'MobileNET', 'InceptionV3', 'NASNET', 'Xception']
plot_chart(values_list, names_of_values)

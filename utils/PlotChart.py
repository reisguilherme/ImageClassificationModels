import matplotlib.pyplot as plt

def plot_chart(values1, values2, labels):
    # Create a bar chart
    plt.figure(figsize=(10, 6))

    # Plot bars for the first set of values (sem data augmentation)
    plt.bar([i - 0.2 for i in range(len(labels))], values1, width=0.4, label='Sem Data Augmentation')

    # Plot bars for the second set of values (com data augmentation)
    plt.bar([i + 0.2 for i in range(len(labels))], values2, width=0.4, label='Com Data Augmentation')

    # Add labels to the axes
    plt.xlabel('Models')
    plt.ylabel('Accuracy')

    # Add a title to the chart
    plt.title('Test Accuracy Comparison')

    # Add values above the bars for the first set of values
    for i, value in enumerate(values1):
        plt.text(i - 0.2, value + 0.5, str(value), ha='center', va='bottom')

    # Add values above the bars for the second set of values
    for i, value in enumerate(values2):
        plt.text(i + 0.2, value + 0.5, str(value), ha='center', va='bottom')

    # Add specific labels for each point on the x-axis
    plt.xticks(range(len(labels)), labels)

    # Display legend
    plt.legend()

    # Display the chart
    plt.show()

# Example of usage
values_list_sem_augmentation = [86.49, 78.38, 75.68, 78.38, 78.08, 78.68, 62.16]
values_list_com_augmentation = [86.49, 89.19, 91.89, 72.97, 81.08, 75.68, 64.86]
names_of_values = ['EfficientNET', 'ConvNeXt', 'DenseNET', 'MobileNET', 'InceptionV3', 'NASNET', 'Xception']
plot_chart(values_list_sem_augmentation, values_list_com_augmentation, names_of_values)

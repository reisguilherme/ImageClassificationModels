import Augmentor
import os

def apply_augmentation(input_folder, output_folder, num_augmentations):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            image_path = os.path.join(root, file)

            # Cria um pipeline para cada imagem
            pipeline = Augmentor.Pipeline(source_directory=os.path.dirname(image_path), output_directory=output_folder)

            # Adiciona operações de aumento de dados
            pipeline.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
            #pipeline.flip_left_right(probability=0.5)
            pipeline.zoom_random(probability=0.5, percentage_area=0.8)
            #pipeline.flip_top_bottom(probability=0.5)
            pipeline.crop_random(probability=0.7, percentage_area=0.9)
            pipeline.random_contrast(probability=0.5, min_factor=0.5, max_factor=1.5)
            pipeline.random_brightness(probability=0.5, min_factor=0.7, max_factor=1.3)

            # Executa o aumento de dados para cada imagem
            pipeline.sample(num_augmentations)


if __name__ == "__main__":
    # Pasta de entrada contendo as imagens originais
    input_folder = "D:\\downloads\\brain_dataset-augmented\\train\\no"

    # Pasta de saída para armazenar as imagens aumentadas
    output_folder = "D:\\downloads\\brain_dataset-augmented\\train-aug\\no"

    # Número de aumentações desejadas por imagem
    num_augmentations = 5

    # Certifica-se de que as pastas de entrada e saída existam
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Aplica o aumento de dados
    apply_augmentation(input_folder, output_folder, num_augmentations)

    print(f"Aumento de dados concluído. Imagens aumentadas salvas em {output_folder}")

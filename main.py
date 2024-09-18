import os
import imageio


def epoch_names(phi, start, end, png_dir):

    files = sorted(os.listdir(png_dir))
    files = [(i.split('_')) for i in files]
    for i in range(len(files)):
        files[i][1] = files[i][1][:-4]
        files[i][0] = int(files[i][0])
        files[i][1] = int(files[i][1])

    sequence = [[phi, i] for i in range(50)]
    names = []
    for i in range(start, end):
        sequence[i][1] = str(sequence[i][1]) + '.png'
        sequence[i][0] = str(sequence[i][0])
        names.append(sequence[i][0] + '_' + sequence[i][1])
    return names
def angle_names(epoch, start, end, png_dir):

    files = sorted(os.listdir(png_dir))
    files = [(i.split('_')) for i in files]
    for i in range(len(files)):
        files[i][1] = files[i][1][:-4]
        files[i][0] = int(files[i][0])
        files[i][1] = int(files[i][1])

    sequence = [[i, epoch] for i in range(50)]
    names = []
    for i in range(start, end):
        sequence[i][1] = str(sequence[i][1]) + '.png'
        sequence[i][0] = str(sequence[i][0])
        names.append(sequence[i][0] + '_' + sequence[i][1])
    return names

def make_gif(files, png_dir):
    from PIL import Image

    # Список для хранения кадров.
    frames = []

    for file in files:
        # Открываем изображение каждого кадра.
        frame = Image.open(f'{png_dir}/{file}')
        # Добавляем кадр в список с кадрами.
        frames.append(frame)

    # Берем первый кадр и в него добавляем оставшееся кадры.
    frames[0].save(
        'homer.gif',
        save_all=True,
        append_images=frames,  # Срез который игнорирует первый кадр.
        optimize=True,
        duration=150,
        loop=0
    )

# make_gif(angle_names(49, 0, 50))
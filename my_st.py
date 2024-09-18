import streamlit as st
import base64
from main import *

file_ = open("homer.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

model = st.radio(
    'Choose encoding method',
    ["Normalization", "Arbuzing"]
)

angle = st.slider("Choose angle", 0, 50, 1)
if st.button("Variate epoch"):
    make_gif(epoch_names(angle, 0, 49, model), model)
epoch = st.slider("Choose epoch", 0, 50, 1)
if st.button("Variate angle"):
    make_gif(angle_names(epoch, 0, 49, model), model)

with st.expander("Инструкция"):
     st.markdown("Всего есть 2500 картинок, которые определяются двумя параметрами: угол, на который повёрнут ближний"
                 " кластер, и эпоха обучения в таком положении")
     st.markdown("Выбирая один из параметров ползунком, вы его фиксируете, оставляя второй параметр переменным. "
                 "В итоге получается гифка из 50 кадров")
     st.markdown("Анимации получились немного косячные, надо будет поменять параметры. Но концепт вот такой вот")
     st.markdown("И ещё, чтобы сгенерить гифку, надо второй раз нажать на кнопку или потеребить слайдер")

st.markdown("Модель обучалась на игрушечном 4-мерном датасете, обычный классификатор из пеннилейна. В статье они тоже "
            "кодируют состояния в амплитуды, с помощью обычного нормирования, а также они используют специальный"
            "алгоритм, который подбирает углы и гейты для кодировки в именно такие амплитуды. Эти углы обзовём Feature "
            "vectors, их сжатая до двух форма показана на гифке")
st.markdown("Датасет сделан из двух гауссовых шумов с центрами на одной оси (центры лежат на одной прямой). При обычной"
            "нормировке данных на единицу, чтобы получить амплитуды, эти два кластера схлопнутся. Для демонстрации этого"
            "я вращал ближний кластер вокруг нуля в плоскости из 0-й и 3-й осей. На картинках как раз показаны проекции"
            "на эту плоскость.")
st.markdown("При выборе обычной нормировки \"Normalization\" видно, как датасеты схлопываются(если они лежат на одной "
            "прямой) и обучение ни к чему не приводит. Если между центрами есть какой-то угол, то можно увидеть, что"
            "классификатор обучается различать кластеры.")
st.markdown("Если выбрать энкодинг Arbuzing, то взаимное положение датасетов уже не играет роли и всё круто ровно "
            "обучается")

# make_gif(angle_names(epoch, 0, 49))

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ===============================
# KONFIGURASI
# ===============================
st.set_page_config(
    page_title="Fish Classification Dashboard",
    page_icon="🐟",
    layout="wide"
)

IMG_SIZE = (224, 224)

CLASS_NAMES = [
    'Catfish',
    'Glass Perchlet',
    'Goby',
    'Gourami',
    'Grass_Carp',
    'Knifefish',
    'Silver Barb',
    'Tilapia'
]

# ===============================
# LOAD MODEL (CACHE)
# ===============================
@st.cache_resource
def load_models():
    cnn = tf.keras.models.load_model(r"D:\Semester 7\mesin learning\Praktikum\uap\models\cnn_fish_classifier_valacc_0.7992.h5")
    eff = tf.keras.models.load_model(r"D:\Semester 7\mesin learning\Praktikum\uap\models\efficientnet_classifier_valacc_0.9958.h5")
    mob = tf.keras.models.load_model(r"D:\Semester 7\mesin learning\Praktikum\uap\models\mobilenetv2_fish_classifier.h5")
    return cnn, eff, mob

cnn_model, eff_model, mob_model = load_models()

# ===============================
# PREPROCESS IMAGE
# ===============================
def preprocess_image(img, model_name):
    img = img.resize(IMG_SIZE)
    img_array = np.array(img)

    if model_name == "EfficientNetB0":
        from tensorflow.keras.applications.efficientnet import preprocess_input
        img_array = preprocess_input(img_array)
    else:
        img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ===============================
# UI
# ===============================
st.title("Klasifikasi Jenis Ikan")
st.markdown(
    """
    Dashboard klasifikasi ikan menggunakan **CNN**, **EfficientNetB0**, dan **MobileNetV2**
    """
)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.header("⚙️ Pengaturan")
model_choice = st.sidebar.selectbox(
    "Pilih Model",
    ["CNN", "EfficientNetB0", "MobileNetV2"]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Gambar Ikan",
    type=["jpg", "jpeg", "png"]
)

# ===============================
# MAIN CONTENT
# ===============================
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(image, caption="Gambar Input", use_column_width=True)

    # ===============================
    # PILIH MODEL
    # ===============================
    if model_choice == "CNN":
        model = cnn_model
    elif model_choice == "EfficientNetB0":
        model = eff_model
    else:
        model = mob_model

    # ===============================
    # PREDIKSI
    # ===============================
    img_array = preprocess_image(image, model_choice)
    preds = model.predict(img_array)
    pred_idx = np.argmax(preds)
    confidence = preds[0][pred_idx] * 100
    pred_class = CLASS_NAMES[pred_idx]

    with col2:
        st.subheader("🔍 Hasil Prediksi")
        st.success(f"**{pred_class}**")
        st.metric("Confidence", f"{confidence:.2f}%")

        st.subheader("📊 Probabilitas Kelas")
        prob_dict = {
            CLASS_NAMES[i]: float(preds[0][i])
            for i in range(len(CLASS_NAMES))
        }
        st.bar_chart(prob_dict)

else:
    st.info("⬅️ Silakan upload gambar ikan melalui sidebar")

# ===============================
# INFO MODEL
# ===============================
st.markdown("---")
st.subheader("📈 Ringkasan Performa Model")

st.table({
    "Model": ["CNN", "EfficientNetB0", "MobileNetV2"],
    "Val Accuracy": ["0.80", "0.99", "0.99"],
    "Kelebihan": [
        "Sederhana & ringan",
        "Akurasi sangat tinggi",
        "Cepat & efisien"
    ]
})

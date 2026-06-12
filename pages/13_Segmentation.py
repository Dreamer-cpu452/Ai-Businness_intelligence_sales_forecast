import streamlit as st

from utils.data_manager import get_data
from utils.segmentation import product_segmentation
from utils.data_manager import get_data
from utils.segmentation import product_segmentation
from utils.visualization import segment_chart

st.title("🎯 Product Segmentation")

df = get_data()

df = product_segmentation(df)
fig = segment_chart(df)

st.success(
    "Segmentation Completed Successfully"
)

st.markdown("---")

st.subheader("Segmented Products")

st.dataframe(

    df[
        [
            "Product",
            "Revenue",
            "Profit",
            "Units_Sold",
            "Segment"
        ]
    ]

)
st.markdown("---")

st.subheader("📊 Segment Visualization")

st.plotly_chart(
    fig,
    use_container_width=True
)
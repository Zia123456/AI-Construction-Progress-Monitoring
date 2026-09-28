import streamlit as st
from PIL import Image
from src.progress_engine import ConstructionProgressMonitor

st.set_page_config(
    page_title="AI Construction Progress Monitoring",
    page_icon="🏗️",
    layout="wide",
)

st.title("🏗️ AI Construction Progress Monitoring")
st.caption("Research prototype for image-based construction-stage classification and progress estimation.")

with st.sidebar:
    st.header("Project Settings")
    model_name = st.selectbox(
        "Vision model",
        ["openai/clip-vit-base-patch32"],
        help="CLIP is used for zero-shot construction-stage classification."
    )
    st.info(
        "This prototype estimates project stage from site imagery. "
        "For research use, validate predictions against annotated site records."
    )

uploaded = st.file_uploader(
    "Upload a construction-site image",
    type=["jpg", "jpeg", "png", "webp"],
)

if uploaded:
    image = Image.open(uploaded).convert("RGB")

    with st.spinner("Analyzing construction progress..."):
        monitor = ConstructionProgressMonitor(model_name=model_name)
        result = monitor.analyze(image)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Site Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("AI Assessment")
        st.metric("Estimated Progress", f"{result.progress_percent:.1f}%")
        st.metric("Estimated Stage", result.stage)

        st.write("### Stage probabilities")
        for stage, probability in result.stage_probabilities:
            st.progress(float(probability), text=f"{stage}: {probability * 100:.1f}%")

    st.divider()
    st.subheader("Research Interpretation")

    if result.progress_percent < 20:
        interpretation = "Early construction stage. Verify whether excavation/foundation activities are underway."
    elif result.progress_percent < 45:
        interpretation = "Structural work appears to be in an early-to-mid stage. Compare with the approved baseline schedule."
    elif result.progress_percent < 70:
        interpretation = "The image indicates an intermediate construction stage. Validate against structural and architectural progress records."
    elif result.progress_percent < 90:
        interpretation = "The project appears to be approaching completion. Review finishing and commissioning activities."
    else:
        interpretation = "The image suggests a late/completion stage. Confirm outstanding works before declaring completion."

    st.write(interpretation)

    st.caption(
        "Important: the estimated percentage is a research-prototype indicator derived "
        "from predicted construction stage, not a certified quantity-surveying measurement."
    )
else:
    st.info("Upload a construction-site image to begin.")
    st.markdown("""
### What this prototype demonstrates

- Zero-shot computer vision for construction-stage classification
- AI-assisted progress estimation
- Human-readable project-control interpretation
- A foundation for future BIM + schedule + site-image integration

### Suggested research workflow

`Site Image → AI Stage Classification → Progress Estimate → Project-Control Dashboard`
""")

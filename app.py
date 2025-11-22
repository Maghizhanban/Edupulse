import streamlit as st

def calculate_cie_marks(internal1, internal2, assignment1, assignment2):
    i1 = (internal1 / 50) * 8
    i2 = (internal2 / 50) * 8
    a1 = (assignment1 / 10) * 4
    a2 = (assignment2 / 10) * 4
    return round(i1 + i2 + a1 + a2, 2)

def calculate_requirements(cie_scored, target_final):
    remaining = target_final - cie_scored

    if remaining <= 0:
        return 0, 0, 0, 0, "🎉 You already reached your target with CIE alone!"

    model_marks = min((remaining / 76) * 10, 10)
    semester_marks = min((remaining / 76) * 60, 60)

    model_percent = round((model_marks / 10) * 100, 2)
    sem_percent = round((semester_marks / 60) * 100, 2)

    return model_marks, semester_marks, model_percent, sem_percent, ""

def feasibility_comment(model_percent, sem_percent):
    if model_percent <= 75 and sem_percent <= 70:
        return "🟢 Very achievable with consistent effort!"
    elif model_percent <= 85 and sem_percent <= 80:
        return "🟡 Possible but requires strong preparation."
    elif model_percent <= 95 and sem_percent <= 90:
        return "🟠 Hard but still possible with full dedication."
    else:
        return "🔴 Almost unrealistic. Consider adjusting target."

def main():
    st.title("🎓 Smart Academic Target & Performance Calculator")

    subjects = ["ENGLISH", "TAMIL", "PHYSICS", "CHEMISTRY", "MATHS", "GRAPHICS"]
    subject = st.selectbox("📘 Select Subject", subjects)

    st.subheader("📝 Enter Completed Internal Marks")
    i1 = st.number_input("Internal 1 (out of 50)", 0.0, 50.0)
    i2 = st.number_input("Internal 2 (out of 50)", 0.0, 50.0)
    a1 = st.number_input("Assignment 1 (out of 10)", 0.0, 10.0)
    a2 = st.number_input("Assignment 2 (out of 10)", 0.0, 10.0)

    if st.button("Calculate CIE Marks"):
        cie_scored = calculate_cie_marks(i1, i2, a1, a2)
        st.session_state["cie_scored"] = cie_scored

    if "cie_scored" in st.session_state:
        cie_scored = st.session_state["cie_scored"]
        st.success(f"📊 CIE Secured: {cie_scored} / 24")

        target = st.slider("🎯 Select Final Target (out of 100)", 50, 100, 85)

        model_marks, sem_marks, model_percent, sem_percent, msg = calculate_requirements(cie_scored, target)

        st.subheader("📉 Requirement Analysis")
        if msg:
            st.success(msg)
        else:
            st.write(f"📝 Model Exam Requirement: **{model_marks:.2f} / 10 → {model_percent}%**")
            st.write(f"📘 Final Semester Requirement: **{sem_marks:.2f} / 60 → {sem_percent}%**")
            st.info(feasibility_comment(model_percent, sem_percent))

            if model_percent >= 95 or sem_percent >= 90:
                st.warning("⚠ Requires near-perfect scores. Consider a realistic goal between 80–88.")

    st.markdown("---")
    st.caption("✨ Smart study planner — built for real students.")

if __name__ == "__main__":
    main()

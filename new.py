import streamlit as st

def calculate_cie_marks(internal1, internal2, assignment1, assignment2):
    i1 = (internal1 / 50) * 8
    i2 = (internal2 / 50) * 8
    a1 = (assignment1 / 10) * 4
    a2 = (assignment2 / 10) * 4
    return round(i1 + i2 + a1 + a2, 2)

def calculate_requirements(cie_scored, target_final):
    total_needed = target_final - cie_scored

    if total_needed <= 0:
        return (0, 0, 0, 0, "🎉 You already achieved the target with internal marks!")

    model_marks_needed = min((total_needed / 76) * 10, 10)
    semester_marks_needed = min((total_needed / 76) * 60, 60)

    model_percent = round((model_marks_needed / 10) * 100, 2)
    semester_percent = round((semester_marks_needed / 60) * 100, 2)

    return model_marks_needed, semester_marks_needed, model_percent, semester_percent, ""

def feasibility_comment(model_percent, sem_percent):
    if model_percent <= 75 and sem_percent <= 70:
        return "🟢 Very achievable with good consistency!"
    elif model_percent <= 85 and sem_percent <= 80:
        return "🟡 Doable, but requires focus and practice."
    elif model_percent <= 95 and sem_percent <= 90:
        return "🟠 Hard, but possible if you give dedicated effort."
    else:
        return "🔴 Extremely difficult. Near perfection required. Consider a realistic target like 80–85."

def main():
    st.title("🎓 Smart Academic Performance & Target Score Bot")
    st.write("Analyze your CIE, Model, and Final Semester targets in seconds!")

    subjects = ["ENGLISH", "TAMIL", "PHYSICS", "CHEMISTRY", "MATHS", "GRAPHICS"]
    subject = st.selectbox("📘 Select Subject", subjects)

    st.subheader("📥 Enter Your Marks")
    i1 = st.number_input("Internal 1 (out of 50)", 0.0, 50.0)
    i2 = st.number_input("Internal 2 (out of 50)", 0.0, 50.0)
    a1 = st.number_input("Assignment 1 (out of 10)", 0.0, 10.0)
    a2 = st.number_input("Assignment 2 (out of 10)", 0.0, 10.0)

    if st.button("Calculate CIE"):
        cie_scored = calculate_cie_marks(i1, i2, a1, a2)
        st.success(f"📊 CIE Secured: {cie_scored} / 24")

        target_final = st.slider("🎯 Final Target (out of 100)", 50, 100)

        model_needed, sem_needed, mod_per, sem_per, msg = calculate_requirements(cie_scored, target_final)

        if msg:
            st.success(msg)
        else:
            st.subheader("📉 Requirements Summary")
            st.write(f"📝 Model Exam: Need {model_needed:.2f}/10 → {mod_per:.2f}%")
            st.write(f"📘 Final Semester: Need {sem_needed:.2f}/60 → {sem_per:.2f}%")

            st.info(feasibility_comment(mod_per, sem_per))

            if mod_per >= 95 or sem_per >= 90:
                st.warning("🏁 Perfect scores needed. Set a more practical goal like 80–85 for safety!")

    # ------------------------ UNIT-BASED LESSON TARGET TRACKER ------------------------
    st.markdown("---")
    st.subheader("📚 Lesson Completion Tracker (Unit Based)")

    units = ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]

    st.write("📌 CIE 1 covers: Unit 1 & Unit 2")
    st.write("📌 CIE 2 covers: Unit 3 & Unit 4")
    st.write("📌 Model & Semester covers: All 5 Units")

    completed_units = st.multiselect(
        "✔️ Select the units you have completed:",
        units,
        default=["Unit 1", "Unit 2", "Unit 3", "Unit 4"]
    )

    completed_count = len(completed_units)
    total_units = len(units)
    percent_completed = (completed_count / total_units) * 100

    st.progress(percent_completed / 100)

    st.write(f"📊 *Completed: {completed_count}/{total_units} units → {percent_completed:.1f}%*")

    if completed_count == 5:
        st.success("🟢 Excellent! All units completed. You're fully ready for semester!")
    elif completed_count == 4:
        st.info("🟡 Good job! Only Unit 5 left — finish it for full readiness.")
    elif completed_count == 3:
        st.warning("🟠 3 units done. Try to complete at least 4 before model exam.")
    elif completed_count == 2:
        st.warning("🟠 You are only ready for CIE 1. Complete more units soon!")
    else:
        st.error("🔴 Very low preparation. Start studying now!")

    expected_marks = min(percent_completed * 1.2, 100)
    st.write(f"📈 *Expected Semester Marks Based on Unit Completion: {expected_marks:.2f} / 100*")

    st.markdown("---")
    st.write("✨ Smart Bot for Academic Planning | Built with ❤️")

if __name__ == "__main__":
    main()

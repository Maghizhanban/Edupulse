import streamlit as st

def calculate_cie_marks(internal1, internal2, assignment1, assignment2):
    i1 = (internal1 / 50) * 8
    i2 = (internal2 / 50) * 8
    a1 = (assignment1 / 10) * 4
    a2 = (assignment2 / 10) * 4
    return round(i1 + i2 + a1 + a2, 2)

def predict_requirements(cie_secured, target):
    remaining = target - cie_secured
    
    if remaining <= 0:
        return {
            "model_required": 0,
            "sem_required": 0,
            "feasible": True,
            "message": "🎉 You have already achieved the target with CIE alone!"
        }
    
    model_required = min((remaining * 10) / 76, 10)
    sem_required = min((remaining * 60) / 76, 60)

    return {
        "model_required": round(model_required, 2),
        "sem_required": round(sem_required, 2),
        "model_percent": round((model_required / 10) * 100, 2),
        "sem_percent": round((sem_required / 60) * 100, 2)
    }

def feasibility_verdict(model_percent, sem_percent):
    if model_percent <= 85 and sem_percent <= 75:
        return "🟢 Highly feasible. You can comfortably reach your target with consistency."
    elif model_percent <= 95 and sem_percent <= 90:
        return "🟡 Challenging but possible. Aim high and stay consistent."
    else:
        return "🔴 Very difficult. Requires near-perfect scores. Reconsider target."

def main():
    st.title("🎓 Smart Academic Performance Bot")
    st.write("📊 Know your CIE status & plan Model + Semester exams wisely!")

    subjects = ["ENGLISH", "TAMIL", "PHYSICS", "CHEMISTRY", "MATHS", "GRAPHICS"]
    subject = st.selectbox("📘 Select Subject", subjects)

    st.subheader(f"📘 Enter Completed Marks for {subject}")

    i1 = st.number_input("Internal 1 (out of 50)", 0.0, 50.0, step=0.5)
    i2 = st.number_input("Internal 2 (out of 50)", 0.0, 50.0, step=0.5)
    a1 = st.number_input("Assignment 1 (out of 10)", 0.0, 10.0, step=0.5)
    a2 = st.number_input("Assignment 2 (out of 10)", 0.0, 10.0, step=0.5)

    if st.button("Calculate CIE ➤"):
        cie_scored = calculate_cie_marks(i1, i2, a1, a2)
        st.success(f"📊 CIE Secured So Far: **{cie_scored} / 24**")

        target = st.number_input("🎯 Enter your Final Target (out of 100)", 50.0, 100.0)

        result = predict_requirements(cie_scored, target)

        if result["model_required"] == 0:
            st.success(result["message"])
        else:
            st.subheader("📉 Requirement Analysis")
            st.write(f"📝 Model Exam (100 → 10): Need **{result['model_required']} / 10** → **{result['model_percent']}%**")
            st.write(f"📘 Final Sem (100 → 60): Need **{result['sem_required']} / 60** → **{result['sem_percent']}%**")

            verdict = feasibility_verdict(result["model_percent"], result["sem_percent"])
            st.info(f"💡 Suggestion: {verdict}")

            # Best realistic suggestion
            if result["model_percent"] > 95 or result["sem_percent"] > 90:
                realistic = round((cie_scored + 8 + 50) / 1.6, 2)
                st.warning(f"🎯 Realistic Safe Target you can aim for: **{realistic}**")

    st.markdown("---")
    st.write("✨ Designed for students to plan smart & score smarter 🚀")

if __name__ == "__main__":
    main()

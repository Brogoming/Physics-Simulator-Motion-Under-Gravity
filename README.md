# Physics-Simulator-Motion-Under-Gravity
An interactive Python application that simulates and visualizes the motion of an object under gravity, including projectile motion, using calculus-based equations of motion. The simulator should offer controls for input parameters and graph the motion over time.

## 🔧 Features & Scope
### MVP (Minimum Viable Product)
- Simulate free fall and projectile motion in 2D
- User inputs:
  - Initial velocity
  - Launch angle
  - Time duration
- Display:
  - Motion graph (x vs t, y vs t, x vs y)
  - Real-time animation of the projectile path
### Stretch Goals (Optional)
- Add air resistance
- Toggle between units (metric/imperial)
- 3D simulation using vpython or pygame
- Export simulation data as CSV or plot image

## 🛠️ Tools & Libraries
| Purpose                   | Tool/Library                       |
| ------------------------- |------------------------------------|
| Math                      | `numpy`                            |
| Plotting                  | `matplotlib`                       |
| Symbolic math (if needed) | `sympy`                            |
| GUI (optional)            | `tkinter`                          |
| Animation                 | `matplotlib.animation` or `pygame` |
| Version Control           | `git + GitHub`                     |

## 📅 Timeline (Today–July 31, 2025)
| Week          | Focus Area                  | Milestones                                                                                               |
| ------------- | --------------------------- | -------------------------------------------------------------------------------------------------------- |
| Jun 12–Jun 18 | Research & Setup            | ✅ Understand equations of motion<br>✅ Define scope (2D vs 3D)<br>✅ Setup project environment             |
| Jun 19–Jun 25 | Core Physics Implementation | ✅ Implement vertical free-fall & horizontal motion<br>✅ Integrate numerical solvers (Euler, Runge-Kutta) |
| Jun 26–Jul 2  | Plotting & Visualization    | ✅ Create 2D motion plots with `matplotlib`<br>✅ Add basic animation                                      |
| Jul 3–Jul 9   | User Interaction            | ✅ Build CLI or GUI (using `tkinter` or `streamlit`)<br>✅ Add parameter input (velocity, angle, etc.)     |
| Jul 10–Jul 20 | Features & Enhancements     | ✅ Air resistance (optional)<br>✅ Real-time animation improvements                                        |
| Jul 21–Jul 27 | Testing & Polishing         | ✅ Test edge cases<br>✅ Refactor code<br>✅ Add comments/documentation                                     |
| Jul 28–Jul 31 | Final Touches               | ✅ Create a demo video (optional)<br>✅ Prepare GitHub README<br>✅ Submit/share your project               |

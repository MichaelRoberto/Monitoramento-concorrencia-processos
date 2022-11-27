from pathlib import Path
import pandas as pd
import plotly
import plotly.figure_factory as ff

# Read Dataframe from Excel file

EXCEL_FILE = Path.cwd() / "Tasks2.xlsx"

print(EXCEL_FILE)

# Read Dataframe from Excel file
df = pd.read_excel(EXCEL_FILE)


fig = ff.create_gantt(df,
                      index_col='Resource', show_colorbar=True,
                      group_tasks=True, title="Processamentos por Rotina", bar_width= 0.25, show_hover_fill=True)
fig.show()

# Save Graph and Export to HTML
plotly.offline.plot(fig, filename="Apresentacao_Gantt.html")
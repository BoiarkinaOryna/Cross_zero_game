import modules.data_base as m_data
import modules.create_line as m_line

def horizontal_victory(value):
    if m_data.list_cells[0] == value and m_data.list_cells[1] == value and m_data.list_cells[2] == value:
        m_line.draw_line_horizontal(-50, 50)
    if m_data.list_cells[3] == value and m_data.list_cells[4] == value and m_data.list_cells[5] == value:
        m_line.draw_line_horizontal(-50, -50)
    elif m_data.list_cells[6] == value and m_data.list_cells[7] == value and m_data.list_cells[8] == value:
        m_line.draw_line_horizontal(-50, -150)
def vertical_victory(value):
    if m_data.list_cells[0] == value and m_data.list_cells[3] == value and m_data.list_cells[6] == value:
        m_line.draw_line_vertical(-50, 50)
    elif m_data.list_cells[1] == value and m_data.list_cells[4] == value and m_data.list_cells[7] == value:
        m_line.draw_line_vertical(50, 50)
    elif m_data.list_cells[2] == value and m_data.list_cells[5] == value and m_data.list_cells[8] == value:
        m_line.draw_line_vertical(150, 50)
def diagonal_victory(value):
    if m_data.list_cells[0] == value and m_data.list_cells[4] == value and m_data.list_cells[8] == value:
        m_line.draw_line_digonal(-50, 50)
    elif m_data.list_cells[2] == value and m_data.list_cells[4] == value and m_data.list_cells[6] == value:
        m_line.draw_line_digonal(150, 50)
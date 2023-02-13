import modules.data_base as m_data
import modules.create_cross as m_cross
import modules.create_zero as m_zero
import modules.victory as m_victory

def who_turn(x, y, index):
    if m_data.step[0] == "cross":
        m_cross.draw_cross(x, y)
        m_data.list_cells[index] = 1
        m_victory.horizontal_victory(1)
        m_victory.vertical_victory(1)
        m_victory.diagonal_victory(1)
        m_data.step[0] = "zero"
    elif m_data.step[0] == "zero":
        m_zero.make_circle(x + 50, y - 100)
        m_data.step[0] = "cross"
        m_data.list_cells[index] = 2
        m_victory.horizontal_victory(2)
        m_victory.vertical_victory(2)
        m_victory.diagonal_victory(2)
    print(m_data.list_cells)
    

        
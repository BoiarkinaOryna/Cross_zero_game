
import modules.processing_turn as m_turn
import modules.data_base as m_data


def click_cell(x,y):
    # Умова першого рядка таблиці 
    if y < 100 and y > 0:
        # Умова першої комірки по х
        if x > -100 and x < 0 and m_data.list_cells[0] == 0:
            m_turn.who_turn(-100, 100, 0)
        # Умова другої комірки по х
        elif x < 100 and x > 0  and m_data.list_cells[1] == 0:
            m_turn.who_turn(0, 100, 1)
        # Умова третьої комірки по х
        elif x > 100 and x < 200  and m_data.list_cells[2] == 0:
            m_turn.who_turn(100, 100, 2)
    # Умова другого рядка таблиці 
    elif y < 0 and y > -100:
        # Умова четвертої комірки по х
        if x > -100 and x < 0  and m_data.list_cells[3] == 0:
            m_turn.who_turn(-100, 0, 3)
        # Умова п'ятої комірки по х
        elif x < 100 and x > 0  and m_data.list_cells[4] == 0:
            m_turn.who_turn(0, 0, 4)
        # Умова шостої комірки по х
        elif x > 100 and x < 200  and m_data.list_cells[5] == 0:
            m_turn.who_turn(100, 0, 5)
    # Умова третього рядка таблиці
    elif y < -100 and y > -200:
        if x > -100 and x < 0 and m_data.list_cells[6] == 0:
            m_turn.who_turn(-100,-100,6)
        elif x < 100 and  x > 0 and m_data.list_cells[7] == 0:
            m_turn.who_turn(0, -100, 7)
        elif x > 100 and x < 200 and m_data.list_cells[8] == 0:
            m_turn.who_turn(100, -100, 8)

            
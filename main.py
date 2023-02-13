import turtle
import modules.create_screen as m_screen
import modules.create_table as m_table
import modules.checking_square_coordinates as m_checking

m_table.draw_table()

m_screen.screen.onclick(m_checking.click_cell, btn= 1, add= True)

turtle.done()
class Colours:
  bg_colour = (82, 49, 20)
  text_colour = (254, 250, 224)
  text_shade = (239, 149, 48)
  default = (31, 21, 10)
  i_colour = (80, 130, 95)
  j_colour = (41, 118, 141)
  l_colour = (229, 123, 37)
  o_colour = (249, 174, 58)
  s_colour = (118, 141, 48)
  t_colour = (130, 81, 112)
  z_colour = (208, 71, 16)

  @classmethod
  def get_colours(cls):
    return [cls.default, cls.i_colour, cls.j_colour, cls.l_colour,
            cls.o_colour, cls.s_colour, cls.t_colour, cls.z_colour]
class Colours:
  bg_colour = (139, 145, 119)
  text_colour = (254, 250, 224)
  default = (153, 160, 131)
  i_colour = (212, 163, 115)
  j_colour = (231, 200, 160)
  l_colour = (250, 237, 205)
  o_colour = (254, 250, 224)
  s_colour = (233, 237, 201)
  t_colour = (204, 213, 174)
  z_colour = (185, 194, 158)

  @classmethod
  def get_colours(cls):
    return [cls.default, cls.i_colour, cls.j_colour, cls.l_colour,
            cls.o_colour, cls.s_colour, cls.t_colour, cls.z_colour]
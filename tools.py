class RequirementNotMet(Exception):
  pass

class ConditionList(object):
  def __init__(self, condition_functions):
    self.condition_functions = condition_funtions
    self.pre_calculated_conditions = map(lambda func: func(), self.condition_functions)
    self.should_calc = False
    self.gets_since_last_calc = 0
    self.cooldown = -1
  
  def setCooldown(self, cooldown):
    self.cooldown = cooldown
    
  def resetCooldown(self):
    self.gets_since_last_calc = 0
  
  def calculate(self):
    self.pre_calculated_conditions = map(lambda func: func(), self.condition_functions)
    self.resetCooldown()
  
  def __iter__(self):
    if self.cooldown == -1:
      self.should_calc = False
    
    else:
      if self.gets_since_last_calc >= self.cooldown:
        self.should_calc == True
      else:
        self.should_calc == False
        self.gets_since_last_calc += 1
    
    if self.should_calc:
      self.calculate()
    return iter(self.pre_calculated_conditions)
  

def require(*conditions):
  for cindex, condition in enumerate(conditions):
    if not condition:
      raise RequirementNotMet(str(cindex))
    

class Button(object):
  def __init__(self, sprite, 

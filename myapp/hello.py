import fire

def hello(name="World"):
  return "SCM TEST TEST TEST Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
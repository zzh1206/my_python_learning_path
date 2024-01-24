#通讯录
_dict = {"张三":133_0000_0000,
              "李四":138_4534_4358}
_dict["王五"] = 186_0000_0000

query = int(input("请输入您要做的任务(1:添加)(2:给人名查)(3:删除)(4:查询所有):"))
if query == 1:
    a = input("您要添加的人名(如果两个人名一样，那么输入‘（人名，年龄）’):")
    b = input("您要添加的号码:")
    _dict[a] = b
else:
    if query == 2:
        c = input("您要查询的人名:")
        if c in _dict:
            print(f"{c}的号码是{_dict[c]}")
        else:
            print("您查询的人名不再字典里") 
    else:
       if query == 3: 
          d = input("您要删除的号码:")
          del _dict[d] 
       else:
           if query == 4: 
               print(_dict)
           else:
                print("输入错误")

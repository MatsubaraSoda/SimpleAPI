def calculate_expression(expression):
    """
    计算表达式API主函数
    使用 eval 进行计算，捕获 eval 的错误

    Args:
        expression (str): 要计算的表达式

    Returns:
        tuple: (result_dict, status_code)
    """
    try:
        # 检查表达式是否为空
        if not expression:
            return {"expression": "", "error": "缺少表达式参数"}, 400

        # 使用 eval 计算表达式
        result = eval(expression)

        # 检查结果是否为数字
        # isinstance(obj, type) 是Python内置函数，用于检查对象是否是指定类型的实例
        # 这里检查 result 是否为 int 或 float 类型
        if not isinstance(result, (int, float)):
            return {
                "expression": expression,
                "error": f"计算结果不是数字: {result}",
            }, 400

        return {"expression": expression, "value": result}, 200

    except (ZeroDivisionError, SyntaxError, NameError, TypeError, ValueError) as e:
        return {"expression": expression, "error": f"计算错误: {str(e)}"}, 400

    except Exception as e:
        return {"expression": expression, "error": f"计算失败: {str(e)}"}, 500

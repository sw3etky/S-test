# src/score_calculator/score_rules.py

def pe_ratio_score(pe_ratio: float) -> int:
    """
    根据市盈率计算评分。较低的PE得分较高，负值返回0。
    """
    if pe_ratio is None or pe_ratio < 0:
        return 0
    if pe_ratio < 10:
        return 10
    elif pe_ratio < 20:
        return 8
    elif pe_ratio < 30:
        return 6
    elif pe_ratio < 40:
        return 4
    else:
        return 2

def roe_score(roe: float) -> int:
    """
    根据净资产收益率计算评分。较高的ROE得分较高。
    """
    if roe is None:
        return 0
    if roe > 20:
        return 10
    elif roe > 15:
        return 8
    elif roe > 10:
        return 6
    elif roe > 5:
        return 4
    else:
        return 2

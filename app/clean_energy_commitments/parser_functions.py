import re


def get_percent(text):
    """
    Return digits labeled with %sign in a string, including possible decimal point
    This is a separate function due to possibility of not matching, and to return better data type
    """
    x = re.search(r"(\d+|\d+\.\d+)%", text)
    if x:
        try:
            return int(re.sub(r"%", "", x.group()))
        except:
            return float(re.sub(r"%", "", x.group()))
    else:
        return


def get_reference_year(text):
    """
    Return digits near 'below YYYY levels' in a string, for use with carbon reduction goal
    This is a separate function due to possibility of not matching, and to return better data type
    """
    x = re.search(r"below (\d{4})", text)
    if x:
        return int(re.sub(r"below ", "", x.group()))
    else:
        return


def get_goal_year(text):
    """
    Return digits near 'by YYYY' in a string, for use with various goal strings
    This is a separate function due to possibility of not matching, and to return better data type
    """
    x = re.search(r"by (\d{4})", text)
    if x:
        return int(re.sub(r"by ", "", x.group()))
    else:
        return


def energy_eff_rank_num(text):
    """
    Parses the 'energy_efficency_rank' column to extract the numeric rank. Original data in the form
    '[XX] is ranked 14th (optional tied-with state names) by the American Council for an Energy-Efficient Economy.'
    """
    x = re.search(r"(\d+)", text)
    if x:
        return int(x.group())
    else:
        return


def clean_energy_commit(text):
    """
    Parses the 'clean_energy_commitment' column to extract commitment details in a dictionary.
    Original data resembles:
    'No'
    'Yes&comma; [XX] has committed in law to 100% clean energy by 2045.'
    "Your governor supports 100% clean energy&comma; but [XX] hasn't made it mandatory."
    """
    if re.search(r"(No)", text):
        return {"commitment": False}
    else:
        pct = get_percent(text)
        by_yr = get_goal_year(text)
        if re.search(r"(governor)", text):
            return {
                "CE_CMT_commitment": "Governor",
                "CE_CMT_mandatory": False,
                "CE_CMT_percent": pct,
                "CE_CMT_by_year": by_yr,
            }
        else:
            return {
                "CE_CMT_commitment": "Law",
                "CE_CMT_mandatory": True,
                "CE_CMT_percent": pct,
                "CE_CMT_by_year": by_yr,
            }


def clean_energy_target_pct(text):
    """
    Parses the 'clean_energy_target_percent' column to extract target details in a dictionary.
    Original data resembles:
    '[XX] does not have a mandatory renewable energy target.'
    '[XX] has a target of 15% renewable or clean energy by 2025.'
    A couple of odd rows: targets in MW instead of %, one 'establsihed a target' as opposed to 'has a target'
    """
    if re.search(r"(does not have)", text):
        return {"CE_TGT_target": False}
    elif re.search(r"(MW)", text):
        # correct for encoded comma
        clean = re.sub(r"&comma;", "", text)
        MW = re.search(r"(\d+) MW", clean)
        by_yr = get_goal_year(text)
        return {
            "CE_TGT_target": True,
            "CE_TGT_MW_target": True,
            "CE_TGT_MW": MW.group(),
            "CE_TGT_pct_target": False,
            "CE_TGT_percent": False,
            "CE_TGT_by_year": by_yr,
        }
    else:
        pct = get_percent(text)
        by_yr = get_goal_year(text)
        return {
            "CE_TGT_target": True,
            "CE_TGT_MW_target": False,
            "CE_TGT_MW": False,
            "CE_TGT_pct_target": True,
            "CE_TGT_percent": pct,
            "CE_TGT_by_year": by_yr,
        }


def carbon_reduction_goal_pct(text):
    """
    Parses the 'carbon_pollution_reduction_goal_percent' column to extract target details in a dictionary.
    Original data resembles:
    'No'
    '[XX] has a nonbinding goal of a 50% reduction in carbon pollution below 2000 levels by 2040.'
    '[XX] has a mandatory goal of an 80% reduction in carbon pollution below 1990 levels by 2050.'
    '[XX] has legislated a goal of 90% reduction in carbon pollution by 2050.'
    '[XX] has a nonbinding goal to be carbon neutral by 2045.'
    '[XX] has a nonbinding goal of a 80% reduction in carbon pollution below 2003 levels.'
    """
    if re.search(r"(No)", text):
        return {"CPR_goal": False}
    else:
        pct = get_percent(text)
        cn = True if re.search(r"(carbon neutral)", text) else False
        ref_yr = get_reference_year(text)
        by_yr = get_goal_year(text)
        if re.search(r"(nonbinding)", text):
            return {
                "CPR_goal": True,
                "CPR_mandatory": False,
                "CPR_percent": pct,
                "CPR_carbon_neutral": cn,
                "CPR_reference_year": ref_yr,
                "CPR_by_year": by_yr,
            }
        else:
            return {
                "CPR_goal": True,
                "CPR_mandatory": True,
                "CPR_percent": pct,
                "CPR_carbon_neutral": cn,
                "CPR_reference_year": ref_yr,
                "CPR_by_year": by_yr,
            }


def elec_vehicle_goals(text):
    """
    Parses the 'electric_vehicle_goals' column column to extract target details in a dictionary.
    Original data resembles:
    'No'
    '[XX] has a zero vehicle emissions mandate with a target that 22% of all new vehicles will be electric by 2025.'
    '[XX] is adopting a zero-emissions vehicle mandate of 22% of new vehicles being electric by 2025.'
    "[XX] has a low-emissions vehicle program which encourages electric vehicles but isn't as strong as a zero-emissions vehicle mandate."
    """
    if re.search(r"(No)", text):
        return {"EV_goal": False}
    else:
        pct = get_percent(text)
        by_yr = get_goal_year(text)
        if re.search(r"(low)", text):
            return {
                "EV_goal": True,
                "EV_mandatory": False,
                "EV_percent": pct,
                "EV_by_year": by_yr,
            }
        else:
            return {
                "EV_goal": True,
                "EV_mandatory": True,
                "EV_percent": pct,
                "EV_by_year": by_yr,
            }


# my instinct is that this is going to do a bunch of repeated searching.
# Not sure how to make it more efficient, or if it's really feasible.
# To discuss: use these in original parsing or do post-process?

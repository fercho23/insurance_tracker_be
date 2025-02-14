# flake8: noqa: E501

PATTERNS = {
    "program_name": r"ProgramName|ProgramTitle",
    "coverage_eligibility": r"CoverageEligibilities|CoverageEligibility",
    "program_type": r"AssistanceType|ProgramType",
    "requirements": [
        {"name": "us_residency", "value": r"EligibilityDetails"},
        {"name": "minimum_age", "value": "18"},
        {"name": "insurance_coverage", "value": r"CoverageEligibilities"},
        {"name": "eligibility_length", "value": r"ExpirationDate"},
    ],
    "benefits": [
        {"name": "max_annual_savings", "value": r"AnnualMax"},
        {"name": "min_out_of_pocket", "value": r"ProgramDetails"},
    ],
    "forms": [{"name": "Enrollment Form", "value": r"EnrollmentURL"}],
    "funding": {
        "evergreen": (
            r"FundLevelType",
            r"FundLevels",
        ),
        "current_funding_level": (
            r"FundLevelType",
            r"FundLevels",
        ),
    },
    "details": {
        "eligibility": r"EligibilityDetails",
        "program": r"ProgramDetails",
        "renewal": (
            r"RenewalMethod",
            r"AddRenewalDetails",
        ),
        "income": (
            r"IncomeReq",
            r"IncomeDetails",
        ),
    },
}

PATTERNS_QUESTIONS = {
    "requirements.0": (
        "Could you tell me if the person is from United States of America?"
        "If the answer is 'yes' return true, if the answer is 'no' return false."
    ),
    "requirements.2": (
        "Could you tell me if the person has insurance coverage?"
        "If the answer is 'yes' return true, if the answer is 'no' return false."
    ),
    "requirements.3": (
        "Could you tell me if the eligibility has insurance coverage?",
        "If the answer is not clear, return 'Data Not Available'.",
    ),
    "benefits.1": (
        "Could you tell me if the person's eligibility has a minimum payment amount?"
        "Represent the value in numbers and if it is not present, return '0.00'."
    ),
    "details.eligibility": (
        "In 1 sentence could you tell me the person's insurance eligibility?"
        "If the answer is not clear, return 'Data Not Available'."
    ),
    "details.program": (
        "In 1 sentence, could you tell me what program the patient is currently under?"
        "If the answer is not clear, return 'Data Not Available'."
    ),
    "details.renewal": (
        "In 1 sentence, could you tell me if the person has renewal and under what conditions?"
        "If the answer is not clear, return 'Data Not Available'."
    ),
}

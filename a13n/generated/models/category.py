from enum import StrEnum


class Category(StrEnum):
    ANSWER_QUALITY = "answer_quality"
    BOUNDARY_VIOLATION = "boundary_violation"
    CONTEXT_GAP = "context_gap"
    INSTRUCTION_ISSUE = "instruction_issue"
    TOOL_DESIGN = "tool_design"
    TOOL_EXECUTION = "tool_execution"
    TOOL_USAGE = "tool_usage"
    UNCLEAR_REQUEST = "unclear_request"
    WORKFLOW_ISSUE = "workflow_issue"

    def __str__(self) -> str:
        return str(self.value)

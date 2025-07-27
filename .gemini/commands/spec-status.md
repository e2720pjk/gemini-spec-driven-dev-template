Show current status and progress for feature: '{{feature_name}}'.

## Process

1.  **Validate Feature Existence**: Check if the directory `.kiro/specs/{{feature_name}}/` exists. If not, inform the user that the feature does not exist.
2.  **Read Spec Files**: Read the following files for the specified feature:
    - `.kiro/specs/{{feature_name}}/spec.json`
    - `.kiro/specs/{{feature_name}}/requirements.md`
    - `.kiro/specs/{{feature_name}}/design.md`
    - `.kiro/specs/{{feature_name}}/tasks.md`
3.  **Read Steering Documents**: Read the steering documents from `.kiro/steering/` (`product.md`, `tech.md`, `structure.md`) for overall project context.
4.  **Analyze Progress**: 
    - Parse `spec.json` to get the current phase, approval statuses, and other metadata.
    - Parse `tasks.md` to count total tasks, completed tasks (by checking `[x]` checkboxes), and remaining tasks. Calculate task completion percentage.
    - Determine phase completion based on `spec.json` approvals.
5.  **Generate Status Report**: Create a comprehensive status report in Markdown format, including:

    ### Specification Overview
    - **Feature Name**: `{{feature_name}}`
    - **Project Description**: (from `spec.json`)
    - **Created At**: (from `spec.json`)
    - **Last Updated**: (from `spec.json`)
    - **Language**: (from `spec.json`)
    - **Current Phase**: (from `spec.json`)
    - **Ready for Implementation**: (from `spec.json`)

    ### Phase Status
    - **Requirements Phase**:
        - Status: (Approved/Not Approved - from `spec.json`)
        - Completion: 100% if approved, 0% otherwise.
        - Details: Summarize key points from `requirements.md`.
    - **Design Phase**:
        - Status: (Approved/Not Approved - from `spec.json`)
        - Completion: 100% if approved, 0% otherwise.
        - Details: Summarize key architectural decisions from `design.md`.
    - **Tasks Phase**:
        - Status: (Approved/Not Approved - from `spec.json`)
        - Total Tasks: (count from `tasks.md`)
        - Completed Tasks: (count from `tasks.md`)
        - Remaining Tasks: (count from `tasks.md`)
        - Completion Percentage: (calculated from `tasks.md`)
        - Details: List next 3 uncompleted tasks.

    ### Implementation Progress (if applicable)
    - If `phase` is `tasks-generated` or later, provide a summary of task completion.

    ### Quality Metrics (Conceptual - based on analysis)
    - **Requirements Clarity**: (e.g., High, Medium, Low - based on `requirements.md` content)
    - **Design Completeness**: (e.g., High, Medium, Low - based on `design.md` content)
    - **Task Granularity**: (e.g., Appropriate, Too Large, Too Small - based on `tasks.md` content)

    ### Recommendations
    - **Next Steps**: Provide clear, actionable next steps based on the current phase and approval status (e.g., "Approve requirements to proceed to design", "Start implementing tasks").
    - **Potential Issues**: Highlight any potential issues or missing information.

    ### Steering Alignment
    - Briefly comment on how the current spec aligns with the project's `product.md`, `tech.md`, and `structure.md`.

6.  **Present Report**: Display the generated status report to the user.
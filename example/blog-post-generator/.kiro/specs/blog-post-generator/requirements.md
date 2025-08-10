# Requirements: blog-post-generator

## 1. Introduction
This feature provides a command-line tool to streamline the creation of basic blog posts in Markdown format. It aims to simplify content generation by guiding the user through inputting essential details (title, author, content) and automatically formatting and saving the post with appropriate metadata.

## 2. Functional Requirements

### 2.1 Blog Post Generation
**User Story:** As a user, I want to generate a new blog post, so that I can quickly create content in Markdown format.

#### Acceptance Criteria
-   **EARS-2.1.1**: WHEN the user initiates the blog post generation THEN the system SHALL prompt for the blog post title.
-   **EARS-2.1.2**: WHEN the user provides the blog post title THEN the system SHALL prompt for the author's name.
-   **EARS-2.1.3**: WHEN the user provides the author's name THEN the system SHALL prompt for the blog post content.
-   **EARS-2.1.4**: WHEN the user provides the blog post content THEN the system SHALL generate a Markdown file.
-   **EARS-2.1.5**: WHEN the Markdown file is generated THEN the system SHALL include a header with metadata (title, author, and creation date).
-   **EARS-2.1.6**: WHEN the Markdown file is generated THEN the system SHALL save the file in a 'posts' directory.
-   **EARS-2.1.7**: WHEN the Markdown file is saved THEN the filename SHALL be the kebab-cased version of the blog post title.
-   **EARS-2.1.8**: IF the 'posts' directory does not exist THEN the system SHALL create it.

## 3. Non-Functional Requirements
-   **Usability**: The command-line interface SHALL be intuitive and easy to use for generating blog posts.
-   **Maintainability**: The code SHALL be well-structured and easy to understand for future modifications.
-   **Portability**: The tool SHALL be runnable on common operating systems (e.g., macOS, Linux, Windows).
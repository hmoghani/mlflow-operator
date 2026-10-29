"""Shared MLflow upgrade scenario state for 3.17-only additions."""

from __future__ import annotations

# Seeded before the upgrade and verified after it. The name is static because the pre-upgrade
# and post-upgrade phases run as separate pytest processes.
SKILL_REGISTRY_STATE = {
    "name": "upgrade-test-skill",
    "description": "Static upgrade-test Skill",
    "skill_tags": {"upgrade-tag-key": "upgrade-tag-value"},
    "version_tags": {"upgrade-version-tag-key": "upgrade-version-tag-value"},
    "alias": "production",
    "versions": [
        {"body": "# Upgrade test Skill\n\nVersion 1 instructions.\n"},
        {"body": "# Upgrade test Skill\n\nVersion 2 instructions.\n"},
    ],
}

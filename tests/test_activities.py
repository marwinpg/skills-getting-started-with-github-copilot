from src.app import activities


def test_get_activities_returns_expected_records(client):
    # Arrange
    expected_activity_names = set(activities)
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    returned_activities = response.json()
    assert set(returned_activities) == expected_activity_names
    for activity in returned_activities.values():
        assert required_fields <= set(activity)
        assert isinstance(activity["participants"], list)

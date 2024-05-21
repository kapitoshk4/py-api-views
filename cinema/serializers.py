from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()

        return instance


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=63)
    last_name = serializers.CharField(max_length=63)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )
        instance.save()

        return instance


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=63)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()

        return instance


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "rows", "seats_in_row"]
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=63)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )
        instance.save()

        return instance

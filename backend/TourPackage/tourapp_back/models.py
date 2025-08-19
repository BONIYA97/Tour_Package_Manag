from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}, {self.country.name}"

class Package(models.Model):
    title = models.CharField(max_length=200)
    source_city = models.ForeignKey(City, related_name="source_city", on_delete=models.CASCADE)
    destination_city = models.ForeignKey(City, related_name="destination_city", on_delete=models.CASCADE)
    description = models.TextField()
    terms = models.TextField()
    photo = models.ImageField(upload_to="packages/")
    def __str__(self):
        return self.title

class Schedule(models.Model):
    package = models.ForeignKey(Package, related_name="schedule", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to="schedules/")
    def __str__(self):
        return f"{self.title} ({self.package.title})"

class Enquiry(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return self.title

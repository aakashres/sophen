from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from ckeditor.fields import RichTextField


TYPE_CHOICES = ((1, 'Afghanistan'),
(2  , 'Albania'),
(3  , 'Algeria'),
(4  , 'Andorra'),
(5  , 'Angola'),
(6  , 'Antigua and Barbuda'),
(7  , 'Argentina'),
(8  , 'Armenia'),
(9  , 'Australia'),
(10 , 'Austria'),
(11 , 'Azerbaijan'),
(12 , 'Bahamas'),
(13 , 'Bahrain'),
(14 , 'Bangladesh'),
(15 , 'Barbados'),
(16 , 'Belarus'),
(17 , 'Belgium'),
(18 , 'Belize'),
(19 , 'Benin'),
(20 , 'Bhutan'),
(21 , 'Bolivia'),
(22 , 'Bosnia and Herzegovina'),
(23 , 'Botswana'),
(24 , 'Brazil'),
(25 , 'Brunei'),
(26 , 'Bulgaria'),
(27 , 'Burkina Faso'),
(28 , 'Burundi'),
(29 , 'Cabo Verde'),
(30 , 'Cambodia'),
(31 , 'Cameroon'),
(32 , 'Canada'),
(33 , 'Central African Republic'),
(34 , 'Chad'),
(35 , 'Chile'),
(36 , 'China'),
(37 , 'Colombia'),
(38 , 'Comoros'),
(39 , 'Democratic Republic of the Congo'),
(40 , 'Republic of the Congo'),
(41 , 'Costa Rica'),
(42 , 'Cote d\'Ivoire'),
(43 , 'Croatia'),
(44 , 'Cuba'),
(45 , 'Cyprus'),
(46 , 'Czech Republic'),
(47 , 'Denmark'),
(48 , 'Djibouti'),
(49 , 'Dominica'),
(50 , 'Dominican Republic'),
(51 , 'Ecuador'),
(52 , 'Egypt'),
(53 , 'El Salvador'),
(54 , 'Equatorial Guinea'),
(55 , 'Eritrea'),
(56 , 'Estonia'),
(57 , 'Ethiopia'),
(58 , 'Fiji'),
(59 , 'Finland'),
(60 , 'France'),
(61 , 'Gabon'),
(62 , 'Gambia'),
(63 , 'Georgia'),
(64 , 'Germany'),
(65 , 'Ghana'),
(66 , 'Greece'),
(67 , 'Grenada'),
(68 , 'Guatemala'),
(69 , 'Guinea'),
(70 , 'Guinea-Bissau'),
(71 , 'Guyana'),
(72 , 'Haiti'),
(73 , 'Honduras'),
(74 , 'Hungary'),
(75 , 'Iceland'),
(76 , 'India'),
(77 , 'Indonesia'),
(78 , 'Iran'),
(79 , 'Iraq'),
(80 , 'Ireland'),
(81 , 'Israel'),
(82 , 'Italy'),
(83 , 'Jamaica'),
(84 , 'Japan'),
(85 , 'Jordan'),
(86 , 'Kazakhstan'),
(87 , 'Kenya'),
(88 , 'Kiribati'),
(89 , 'Kosovo'),
(90 , 'Kuwait'),
(91 , 'Kyrgyzstan'),
(92 , 'Laos'),
(93 , 'Latvia'),
(94 , 'Lebanon'),
(95 , 'Lesotho'),
(96 , 'Liberia'),
(97 , 'Libya'),
(98 , 'Liechtenstein'),
(99 , 'Lithuania'),
(100, 'Luxembourg'),
(101, 'Macedonia'),
(102, 'Madagascar'),
(103, 'Malawi'),
(104, 'Malaysia'),
(105, 'Maldives'),
(106, 'Mali'),
(107, 'Malta'),
(108, 'Marshall Islands'),
(109, 'Mauritania'),
(110, 'Mauritius'),
(111, 'Mexico'),
(112, 'Micronesia'),
(113, 'Moldova'),
(114, 'Monaco'),
(115, 'Mongolia'),
(116, 'Montenegro'),
(117, 'Morocco'),
(118, 'Mozambique'),
(119, 'Myanmar'),
(120, 'Namibia'),
(121, 'Nauru'),
(122, 'Nepal'),
(123, 'Netherlands'),
(124, 'New Zealand'),
(125, 'Nicaragua'),
(126, 'Niger'),
(127, 'Nigeria'),
(128, 'North Korea'),
(129, 'Norway'),
(130, 'Oman'),
(131, 'Pakistan'),
(132, 'Palau'),
(133, 'Palestine'),
(134, 'Panama'),
(135, 'Papua New Guinea'),
(136, 'Paraguay'),
(137, 'Peru'),
(138, 'Philippines'),
(139, 'Poland'),
(140, 'Portugal'),
(141, 'Qatar'),
(142, 'Romania'),
(143, 'Russia'),
(144, 'Rwanda'),
(145, 'Saint Kitts and Nevis'),
(146, 'Saint Lucia'),
(147, 'Saint Vincent and the Grenadines'),
(148, 'Samoa'),
(149, 'San Marino'),
(150, 'Sao Tome and Principe'),
(151, 'Saudi Arabia'),
(152, 'Senegal'),
(153, 'Serbia'),
(154, 'Seychelles'),
(155, 'Sierra Leone'),
(156, 'Singapore'),
(157, 'Slovakia'),
(158, 'Slovenia'),
(159, 'Solomon Islands'),
(160, 'Somalia'),
(161, 'South Africa'),
(162, 'South Korea'),
(163, 'South Sudan'),
(164, 'Spain'),
(165, 'Sri Lanka'),
(166, 'Sudan'),
(167, 'Suriname'),
(168, 'Swaziland'),
(169, 'Sweden'),
(170, 'Switzerland'),
(171, 'Syria'),
(172, 'Taiwan'),
(173, 'Tajikistan'),
(174, 'Tanzania'),
(175, 'Thailand'),
(176, 'Timor-Leste'),
(177, 'Togo'),
(178, 'Tonga'),
(179, 'Trinidad and Tobago'),
(180, 'Tunisia'),
(181, 'Turkey'),
(182, 'Turkmenistan'),
(183, 'Tuvalu'),
(184, 'Uganda'),
(185, 'Ukraine'),
(186, 'United Arab Emirates'),
(187, 'United Kingdom'),
(188, 'United States of America'),
(189, 'Uruguay'),
(190, 'Uzbekistan'),
(191, 'Vanuatu'),
(192, 'Vatican City'),
(193, 'Venezuela'),
(194, 'Vietnam'),
(195, 'Yemen'),
(196, 'Zambia'),
(197, 'Zimbabwe'))

# Create your models here.

class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


class Page(Timestampable):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextField()

    def __str__(self):
        return self.title


def uploadEventPhoto(instance, filename):
    return "%s/%s/%s" % ('event', instance.title, filename)


class Event(Timestampable):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    event_date = models.DateTimeField()

    description = RichTextField()

    photo = models.ImageField(upload_to=uploadEventPhoto,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.title


class Menu(Timestampable):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=50, help_text='/pages/1/')
    priority = models.IntegerField(
        help_text='Lower number comes first in menu', null=False, blank=False)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ['priority', ]

    @staticmethod
    def get_root():
        return Menu.objects.filter(title="root").get()

    def not_deleted_children(self):
        return self.children.filter(deleted_at=None)

    def __str__(self):
        if self.parent:
            if self.parent.title != "root":
                return self.parent.title + ' : ' + self.title
        return self.title


def uploadSliderPhoto(instance, filename):
    return "%s/%s" % ('slider' , get_random_string(length=5)+filename)


class Slider(Timestampable):
    photo = models.ImageField(upload_to='slider/',
                              null=True,
                              blank=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)


def uploadGalleryPhoto(instance, filename):
    date_time = str(timezone.now())
    return "%s/%s/%s" % ('gallery', str(date_time), filename)


class Gallery(Timestampable):
    photo = models.ImageField(upload_to=uploadGalleryPhoto,
                              null=True,
                              blank=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return str(self.pk)


def uploadFile(instance, filename):
    date_time = str(timezone.now())
    return "%s/%s/%s" % ('file', str(date_time), filename)


class File(Timestampable):
    file = models.FileField(upload_to=uploadFile,
                            null=True,
                            blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class ConferenceMember(Timestampable):
    company_name = models.CharField('Name of Company', max_length=255)
    address_1 = models.TextField('Address 1')
    address_2 = models.TextField('Address 2', null=True, blank=True)
    town_city = models.CharField('Town/City', max_length=255)
    state = models.CharField('Name of State', max_length=512, null=True, blank=True)
    postal_zip = models.CharField('Postal/Zip', max_length=255)
    country = models.IntegerField(choices=TYPE_CHOICES, default=1)
    business_type = models.CharField('Type of Business', max_length=512, null=True, blank=True)
    contact_person = models.CharField('Contact Person', max_length=512)
    contact_for_payment = models.CharField('Contact Person for Payment', max_length=512)
    telephone = models.CharField('Telephone', max_length=512, null=True, blank=True)
    fax = models.CharField('Fax', max_length=512, null=True, blank=True)
    
    mobile = models.CharField('Mobile', max_length=512, null=True, blank=True)
    email = models.CharField('Email', max_length=512)
    signature = models.CharField('Signature (Full Name, Date)', max_length=512)
    
    

    def __str__(self):
        return str(company_name)



class Member(Timestampable):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=100)
    dob = models.DateField()
    photo = models.ImageField()
    permanent_address = models.CharField(max_length=255)
    mailing_address = models.CharField(max_length=255)
    degree_1 = models.CharField(max_length=100)
    major_1 = models.CharField(max_length=100)
    institution_1 = models.CharField(max_length=100)
    year_1 = models.CharField(max_length=4)
    degree_2 = models.CharField(max_length=100, null=True, blank=True)
    major_2 = models.CharField(max_length=100, null=True, blank=True)
    institution_2 = models.CharField(max_length=100, null=True, blank=True)
    year_2 = models.CharField(max_length=4, null=True, blank=True)
    degree_3 = models.CharField(max_length=100, null=True, blank=True)
    major_3 = models.CharField(max_length=100, null=True, blank=True)
    institution_3 = models.CharField(max_length=100, null=True, blank=True)
    year_3 = models.CharField(max_length=4, null=True, blank=True)
    degree_4 = models.CharField(max_length=100, null=True, blank=True)
    major_4 = models.CharField(max_length=100, null=True, blank=True)
    institution_4 = models.CharField(max_length=100, null=True, blank=True)
    year_4 = models.CharField(max_length=4, null=True, blank=True)
    from_1 = models.DateField()
    to_1 = models.DateField()
    organization_1 = models.CharField(max_length=255)
    description_of_work_1 = models.CharField(max_length=255)
    from_2 = models.DateField(null=True, blank=True)
    to_2 = models.DateField(null=True, blank=True)
    organization_2 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_2 = models.CharField(
        max_length=255, null=True, blank=True)
    from_3 = models.DateField(null=True, blank=True)
    to_3 = models.DateField(null=True, blank=True)
    organization_3 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_3 = models.CharField(
        max_length=255, null=True, blank=True)
    from_4 = models.DateField(null=True, blank=True)
    to_4 = models.DateField(null=True, blank=True)
    organization_4 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_4 = models.CharField(
        max_length=255, null=True, blank=True)
    from_5 = models.DateField(null=True, blank=True)
    to_5 = models.DateField(null=True, blank=True)
    organization_5 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_5 = models.CharField(
        max_length=255, null=True, blank=True)
    membership_of_any_other = models.CharField(
        max_length=255, null=True, blank=True)
    present_position = models.CharField(max_length=255, null=True, blank=True)
    employeer = models.CharField(max_length=255, null=True, blank=True)
    office_address = models.CharField(max_length=255, blank=True, null=True)
    recommenders_name = models.CharField(max_length=255, null=True, blank=True)
    membership_no = models.IntegerField(null=True, blank=True)
    membership_status = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

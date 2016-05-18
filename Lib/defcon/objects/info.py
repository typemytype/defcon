from __future__ import absolute_import
# this file was generated by infoObjectGenerator.py.
# this file should not be edited by hand.

import weakref
from warnings import warn
import ufoLib
from defcon.objects.base import BaseObject
from defcon.objects.guideline import Guideline
from copy import copy


def init_property(cls, name, setup):
    setterName = '_set_{0}'.format(name)
    getterName = '_get_{0}'.format(name)
    privateName = '_{0}'.format(name)

    doc, default = setup

    def getter(self):
        return getattr(self, privateName)
    getter.__name__ = getterName

    def setter(self, value):
        oldValue = getattr(self, privateName)
        if oldValue == value:
            return
        if value is None:
            value = copy(default)
        else:
            valid = ufoLib.validateFontInfoVersion3ValueForAttribute(name, value)
            if not valid:
                raise ValueError("Invalid value ({0}) for attribute {1}.".format(repr(value), name))
        setattr(self, privateName, value)
        self.postNotification("Info.ValueChanged", data=dict(attribute=name, oldValue=oldValue, newValue=value))
        self.dirty = True
    setter.__name__ = setterName

    prop = property(getter, setter, doc)

    setattr(cls, setterName, setter)
    setattr(cls, getterName, getter)
    setattr(cls, name, prop)

def init_properties(cls):
    for name in cls._properties:
        init_property(cls, name, cls._properties[name])
    return cls

@init_properties
class Info(BaseObject):
    """
    This object represents info values.

    **This object posts the following notifications:**

    ===========================
    Name
    ===========================
    Info.Changed
    Info.BeginUndo
    Info.EndUndo
    Info.BeginRedo
    Info.EndRedo
    Info.ValueChanged
    Info.GuidelinesChanged
    Info.GuidelineWillBeDeleted
    ===========================

    **Note:** The documentation strings here were automatically generated
    from the `UFO specification <http://unifiedfontobject.org/filestructure/fontinfo.html>`_.
    """

    changeNotificationName = "Info.Changed"
    beginUndoNotificationName = "Info.BeginUndo"
    endUndoNotificationName = "Info.EndUndo"
    beginRedoNotificationName = "Info.BeginRedo"
    endRedoNotificationName = "Info.EndRedo"
    representationFactories = {}

    def __init__(self, font=None, guidelineClass=None):
        if font is not None:
            font = weakref.ref(font)
        self._font = font
        super(Info, self).__init__()
        self.beginSelfNotificationObservation()
        self._identifiers = set()
        if guidelineClass is None:
            guidelineClass = Guideline
        self._guidelineClass = guidelineClass

        self._guidelines = []

        # init private property attributes
        for name in self._properties:
            _, default = self._properties[name]
            setattr(self, '_'+name, copy(default))

    def __del__(self):
        super(Info, self).__del__()
        self._guidelines = None

    def getParent(self):
        return self.font


    def _get_font(self):
        if self._font is not None:
            return self._font()
        return None

    font = property(_get_font, doc="The :class:`Font` that this object belongs to.")

    # ----------
    # Properties
    # ----------
    _properties = {
        "ascender": ("Ascender value. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "capHeight": ("Cap height value. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "copyright": ("Copyright statement. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "descender": ("Descender value. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "familyName": ("Family name. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "italicAngle": ("Italic angle. This must be an angle in counter-clockwise degrees from the vertical. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "macintoshFONDFamilyID": ("Family ID number. Corresponds to the ffFamID in the FOND resource. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "macintoshFONDName": ("Font name for the FOND resource. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "note": ("Arbitrary note about the font. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeGaspRangeRecords": ("A list of gasp Range Records. These must be sorted in ascending order based on the <code>rangeMaxPPEM</code> value of the record. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHeadCreated": ("Creation date. Expressed as a string of the format \"YYYY/MM/DD HH:MM:SS\". \"YYYY/MM/DD\" is year/month/day. The month must be in the range 1-12 and the day must be in the range 1-end of month. \"HH:MM:SS\" is hour:minute:second. The hour must be in the range 0:23. The minute and second must each be in the range 0-59. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHeadFlags": ("A list of bit numbers indicating the flags. The bit numbers are listed in the OpenType head specification. Corresponds to the OpenType head table <code>flags</code> field. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHeadLowestRecPPEM": ("Smallest readable size in pixels. Corresponds to the OpenType head table <code>lowestRecPPEM</code> field. This should be a non-negative integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHheaAscender": ("Ascender value. Corresponds to the OpenType hhea table <code>Ascender</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHheaCaretOffset": ("Caret offset value. Corresponds to the OpenType hhea table <code>caretOffset</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHheaCaretSlopeRise": ("Caret slope rise value. Corresponds to the OpenType hhea table <code>caretSlopeRise</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHheaCaretSlopeRun": ("Caret slope run value. Corresponds to the OpenType hhea table <code>caretSlopeRun</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHheaDescender": ("Descender value. Corresponds to the OpenType hhea table <code>Descender</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeHheaLineGap": ("Line gap value. Corresponds to the OpenType hhea table <code>LineGap</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameCompatibleFullName": ("Compatible full name. Corresponds to the OpenType name table name ID 18. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameDescription": ("Description of the font. Corresponds to the OpenType name table name ID 10. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameDesigner": ("Designer name. Corresponds to the OpenType name table name ID 9. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameDesignerURL": ("URL for the designer. Corresponds to the OpenType name table name ID 12. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameLicense": ("License text. Corresponds to the OpenType name table name ID 13. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameLicenseURL": ("URL for the license. Corresponds to the OpenType name table name ID 14. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameManufacturer": ("Manufacturer name. Corresponds to the OpenType name table name ID 8. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameManufacturerURL": ("Manufacturer URL. Corresponds to the OpenType name table name ID 11. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNamePreferredFamilyName": ("Preferred family name. Corresponds to the OpenType name table name ID 16. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNamePreferredSubfamilyName": ("Preferred subfamily name. Corresponds to the OpenType name table name ID 17. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameRecords": ("A list of name records. This name record storage area is intended for records that require platform, encoding and or language localization. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameSampleText": ("Sample text. Corresponds to the OpenType name table name ID 19. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameUniqueID": ("Unique ID string. Corresponds to the OpenType name table name ID 3. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameVersion": ("Version string. Corresponds to the OpenType name table name ID 5. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameWWSFamilyName": ("WWS family name. Corresponds to the OpenType name table name ID 21. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeNameWWSSubfamilyName": ("WWS Subfamily name. Corresponds to the OpenType name table name ID 22. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2CodePageRanges": ("A list of bit numbers that are supported code page ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table <code>ulCodePageRange1</code> and <code>ulCodePageRange2</code> fields. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2FamilyClass": ("Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, must be in the range 0-14. The second number, representing the subclass, must be in the range 0-15. The numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table <code>sFamilyClass</code> field. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2Panose": ("The list must contain 10 non-negative integers that represent the setting for each category in the Panose specification. The integers correspond with the option numbers in each of the Panose categories. This corresponds to the OpenType OS/2 table <code>Panose</code> field. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2Selection": ("A list of bit numbers indicating the bits that should be set in fsSelection. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table <code>selection</code> field. Note: Bits 0 (italic), 5 (bold) and 6 (regular) must not be set here. These bits should be taken from the generic styleMapStyle attribute. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2StrikeoutPosition": ("Strikeout position. Corresponds to the OpenType OS/2 table <code>yStrikeoutPosition</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2StrikeoutSize": ("Strikeout size. Corresponds to the OpenType OS/2 table <code>yStrikeoutSize</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SubscriptXOffset": ("Subscript x offset. Corresponds to the OpenType OS/2 table <code>ySubscriptXOffset</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SubscriptXSize": ("Subscript horizontal font size. Corresponds to the OpenType OS/2 table <code>ySubscriptXSize</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SubscriptYOffset": ("Subscript y offset. Corresponds to the OpenType OS/2 table <code>ySubscriptYOffset</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SubscriptYSize": ("Subscript vertical font size. Corresponds to the OpenType OS/2 table <code>ySubscriptYSize</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SuperscriptXOffset": ("Superscript x offset. Corresponds to the OpenType OS/2 table <code>ySuperscriptXOffset</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SuperscriptXSize": ("Superscript horizontal font size. Corresponds to the OpenType OS/2 table <code>ySuperscriptXSize</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SuperscriptYOffset": ("Superscript y offset. Corresponds to the OpenType OS/2 table <code>ySuperscriptYOffset</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2SuperscriptYSize": ("Superscript vertical font size. Corresponds to the OpenType OS/2 table <code>ySuperscriptYSize</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2Type": ("A list of bit numbers indicating the embedding type. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table <code>fsType</code> field. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2TypoAscender": ("Ascender value. Corresponds to the OpenType OS/2 table <code>sTypoAscender</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2TypoDescender": ("Descender value. Corresponds to the OpenType OS/2 table <code>sTypoDescender</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2TypoLineGap": ("Line gap value. Corresponds to the OpenType OS/2 table <code>sTypoLineGap</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2UnicodeRanges": ("A list of bit numbers that are supported Unicode ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table <code>ulUnicodeRange1</code>, <code>ulUnicodeRange2</code>, <code>ulUnicodeRange3</code> and <code>ulUnicodeRange4</code> fields. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2VendorID": ("Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table <code>achVendID</code> field. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2WeightClass": ("Weight class value. Must be a non-negative integer. Corresponds to the OpenType OS/2 table <code>usWeightClass</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2WidthClass": ("Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table <code>usWidthClass</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2WinAscent": ("Ascender value. Corresponds to the OpenType OS/2 table <code>usWinAscent</code> field. This should be a non-negative integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeOS2WinDescent": ("Descender value. Corresponds to the OpenType OS/2 table <code>usWinDescent</code> field. This should be a non-negative integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeVheaCaretOffset": ("Caret offset value. Corresponds to the OpenType vhea table <code>caretOffset</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeVheaCaretSlopeRise": ("Caret slope rise value. Corresponds to the OpenType vhea table <code>caretSlopeRise</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeVheaCaretSlopeRun": ("Caret slope run value. Corresponds to the OpenType vhea table <code>caretSlopeRun</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeVheaVertTypoAscender": ("Ascender value. Corresponds to the OpenType vhea table <code>vertTypoAscender</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeVheaVertTypoDescender": ("Descender value. Corresponds to the OpenType vhea table <code>vertTypoDescender</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "openTypeVheaVertTypoLineGap": ("Line gap value. Corresponds to the OpenType vhea table <code>vertTypoLineGap</code> field. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "postscriptBlueFuzz": ("BlueFuzz value. This corresponds to the Type 1/CFF <code>BlueFuzz</code> field. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptBlueScale": ("BlueScale value. This corresponds to the Type 1/CFF <code>BlueScale</code> field. This should be a float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptBlueShift": ("BlueShift value. This corresponds to the Type 1/CFF <code>BlueShift</code> field. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptBlueValues": ("A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list. Setting this will post an *Info.Changed* notification.", []),
        "postscriptDefaultCharacter": ("The name of the glyph that should be used as the default character in PFM files. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "postscriptDefaultWidthX": ("Default width for glyphs. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptFamilyBlues": ("A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list. Setting this will post an *Info.Changed* notification.", []),
        "postscriptFamilyOtherBlues": ("A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list. Setting this will post an *Info.Changed* notification.", []),
        "postscriptFontName": ("Name to be used for the <code>FontName</code> field in Type 1/CFF table. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "postscriptForceBold": ("Indicates how the Type 1/CFF <code>ForceBold</code> field should be set. This should be a boolean. Setting this will post an *Info.Changed* notification.", None),
        "postscriptFullName": ("Name to be used for the <code>FullName</code> field in Type 1/CFF table. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "postscriptIsFixedPitch": ("Indicates if the font is monospaced. An authoring tool could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF <code>isFixedPitched</code> field This should be a boolean. Setting this will post an *Info.Changed* notification.", None),
        "postscriptNominalWidthX": ("Nominal width for glyphs. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptOtherBlues": ("A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list. Setting this will post an *Info.Changed* notification.", []),
        "postscriptSlantAngle": ("Artificial slant angle. This must be an angle in counter-clockwise degrees from the vertical. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptStemSnapH": ("List of horizontal stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF <code>StemSnapH</code> field. This should be a list. Setting this will post an *Info.Changed* notification.", []),
        "postscriptStemSnapV": ("List of vertical stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF <code>StemSnapV</code> field. This should be a list. Setting this will post an *Info.Changed* notification.", []),
        "postscriptUnderlinePosition": ("Underline position value. Corresponds to the Type 1/CFF/post table <code>UnderlinePosition</code> field. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptUnderlineThickness": ("Underline thickness value. Corresponds to the Type 1/CFF/post table <code>UnderlineThickness</code> field. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "postscriptUniqueID": ("A unique ID number as defined in the Type 1/CFF specification. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "postscriptWeightName": ("A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the <code>openTypeOS2WeightClass</code> value. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "postscriptWindowsCharacterSet": ("The Windows character set. The values are defined below. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "styleMapFamilyName": ("Family name used for bold, italic and bold italic style mapping. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "styleMapStyleName": ("Style map style. The possible values are regular, italic, bold and bold italic. These are case sensitive. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "styleName": ("Style name. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "trademark": ("Trademark statement. This should be a string. Setting this will post an *Info.Changed* notification.", None),
        "unitsPerEm": ("Units per em. This should be a non-negative integer or float. Setting this will post an *Info.Changed* notification.", None),
        "versionMajor": ("Major version. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
        "versionMinor": ("Minor version. This should be a non-negative integer. Setting this will post an *Info.Changed* notification.", None),
        "woffMajorVersion": ("Major version of the font. This should be a non-negative integer. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataCopyright": ("Font copyright. Corresponds to the WOFF <code>copyright</code> element. The dictionary must follow the WOFF Metadata Copyright Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataCredits": ("Font credits. Corresponds to the WOFF <code>credits</code> element. The dictionary must follow the WOFF Metadata Credits Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataDescription": ("Font description. Corresponds to the WOFF <code>description</code> element. The dictionary must follow the WOFF Metadata Description Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataExtensions": ("List of metadata extension records. The dictionaries must follow the WOFF Metadata Extension Record structure. There must be at least one extension record in the list. This should be a list. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataLicense": ("Font description. Corresponds to the WOFF <code>license</code> element. The dictionary must follow the WOFF Metadata License Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataLicensee": ("Font licensee. Corresponds to the WOFF <code>licensee</code> element. The dictionary must follow the WOFF Metadata Licensee Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataTrademark": ("Font trademark. Corresponds to the WOFF <code>trademark</code> element. The dictionary must follow the WOFF Metadata Trademark Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataUniqueID": ("Identification string. Corresponds to the WOFF <code>uniqueid</code>. The dictionary must follow the WOFF Metadata Unique ID Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMetadataVendor": ("Font vendor. Corresponds to the WOFF <code>vendor</code> element. The dictionary must follow the the WOFF Metadata Vendor Record structure. This should be a dictionary. Setting this will post an *Info.Changed* notification.", None),
        "woffMinorVersion": ("Minor version of the font. This should be a non-negative integer. Setting this will post an *Info.Changed* notification.", None),
        "xHeight": ("x-height value. This should be a integer or float. Setting this will post an *Info.Changed* notification.", None),
        "year": ("The year the font was created. This attribute is deprecated as of version 2. It's presence should not be relied upon by authoring tools. However, it may occur in a font's info so authoring tools should preserve it if present. This should be a integer. Setting this will post an *Info.Changed* notification.", None),
    }

    # -----------
    # Identifiers
    # -----------

    def _get_identifiers(self):
        return self._identifiers

    identifiers = property(_get_identifiers, doc="Set of identifiers for the info. This is primarily for internal use.")

    # ----------
    # Guidelines
    # ----------

    def _get_guidelines(self):
        return list(self._guidelines)

    def _set_guidelines(self, value):
        self.clearGuidelines()
        self.holdNotifications()
        for guideline in value:
            self.appendGuideline(guideline)
        self.releaseHeldNotifications()

    guidelines = property(_get_guidelines, _set_guidelines, doc="An ordered list of :class:`Guideline` objects stored in the info. Setting this will post a *Info.Changed* notification along with any notifications posted by the :py:meth:`Info.appendGuideline` and :py:meth:`Info.clearGuidelines` methods.")

    def instantiateGuideline(self, guidelineDict=None):
        guideline = self._guidelineClass(
            fontInfo=self,
            guidelineDict=guidelineDict
        )
        return guideline

    def beginSelfGuidelineNotificationObservation(self, guideline):
        if guideline.dispatcher is None:
            return
        guideline.addObserver(observer=self, methodName="_guidelineChanged", notification="Guideline.Changed")

    def endSelfGuidelineNotificationObservation(self, guideline):
        if guideline.dispatcher is None:
            return
        guideline.endSelfNotificationObservation()
        guideline.removeObserver(observer=self, notification="Guideline.Changed")

    def appendGuideline(self, guideline):
        """
        Append **guideline** to the info. The guideline must be a defcon
        :class:`Guideline` object or a subclass of that object. An error
        will be raised if the guideline's identifier conflicts with any of
        the identifiers within the info.

        This will post *Info.GuidelinesChanged* and *Info.Changed* notifications.
        """
        self.insertGuideline(len(self._guidelines), guideline)

    def insertGuideline(self, index, guideline):
        """
        Insert **guideline** into the info at index. The guideline
        must be a defcon :class:`Guideline` object or a subclass
        of that object. An error will be raised if the guideline's
        identifier conflicts with any of the identifiers within
        the info.

        This will post *Info.GuidelinesChanged* and *Info.Changed* notifications.
        """
        try:
            assert guideline.fontInfo != self
        except AttributeError:
            pass
        if not isinstance(guideline, self._guidelineClass):
            guideline = self.instantiateGuideline(guidelineDict=guideline)
        assert guideline.fontInfo in (self, None), "This guideline belongs to another font."
        if guideline.fontInfo is None:
            assert guideline.glyph is None, "This guideline belongs to a glyph."
        if guideline.fontInfo is None:
            if guideline.identifier is not None:
                identifiers = self._identifiers
                assert guideline.identifier not in identifiers
                if guideline.identifier is not None:
                    identifiers.add(guideline.identifier)
            guideline.fontInfo = self
            guideline.beginSelfNotificationObservation()
        self.beginSelfGuidelineNotificationObservation(guideline)
        self._guidelines.insert(index, guideline)
        self.postNotification("Info.GuidelinesChanged")
        self.dirty = True

    def removeGuideline(self, guideline):
        """
        Remove **guideline** from the info.

        This will post a *Glyph.Changed* notification.
        """
        self.postNotification(notification="Info.GuidelineWillBeDeleted", data=dict(object=guideline))
        if guideline.identifier is not None:
            self._identifiers.remove(guideline.identifier)
        self._guidelines.remove(guideline)
        self.endSelfGuidelineNotificationObservation(guideline)
        self.postNotification("Info.GuidelinesChanged")
        self.dirty = True

    def guidelineIndex(self, guideline):
        """
        Get the index for **guideline**.
        """
        return self._guidelines.index(guideline)

    def clearGuidelines(self):
        """
        Clear all guidelines from the info.

        This posts a *Glyph.Changed* notification.
        """
        self.holdNotifications()
        for guideline in reversed(self._guidelines):
            self.removeGuideline(guideline)
        self.releaseHeldNotifications()

    # ------------------------
    # Notification Observation
    # ------------------------

    def endSelfNotificationObservation(self):
        if self.dispatcher is None:
            return
        for guideline in self.guidelines:
            self.endSelfGuidelineNotificationObservation(guideline)
        super(Info, self).endSelfNotificationObservation()
        self._font = None

    def _guidelineChanged(self, notification):
        self.postNotification("Info.GuidelinesChanged")
        self.dirty = True

    # -----------------------------
    # Serialization/Deserialization
    # -----------------------------

    def getDataForSerialization(self, **kwargs):
        from functools import partial

        simple_get = partial(getattr, self)
        serialize = lambda item: item.getDataForSerialization()
        serialized_get = lambda key: serialize(simple_get(key))
        serialized_list_get = lambda key: [serialize(item) for item in simple_get(key)]

        getters = [
            ('guidelines', serialized_list_get)
        ]
        for name in self._properties:
            if getattr(self, '_' + name) is None:
                continue
            getters.append((name, simple_get))

        return self._serialize(getters, **kwargs)

    def setDataFromSerialization(self, data):
        from functools import partial

        simple_set = partial(setattr, self)

        def set_guidelines(key, data):
            guides = []
            for d in data:
                guide = self.instantiateGuideline()
                guide.setDataFromSerialization(d)
                guides.append(guide)
            simple_set(key, guides)

        setters = [(name, simple_set) for name in self._properties]
        setters.append(('guidelines', set_guidelines))

        self._identifiers = set()
        for name, setter in setters:
            if name not in data:
                continue
            setter(name, data[name])

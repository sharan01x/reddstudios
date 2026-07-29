#!/usr/bin/env python3
"""
# ---------------------------------------------------------------------------
#                         LAW AS CODE (KARNATAKA)
#            Transfer of Property, 1882 -- compiled into Python
#
#  This program is a compiler. It does not compile source into machine code.
#  It compiles human longing into legal property.
#
#  Each function is a statute. Each exception is a void.
#  Each comment is a magistrate's marginalia.
#
#  To run:   python3 lawascode.py
#  To read:  open in any editor. The law is the code.
# ---------------------------------------------------------------------------
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List, Dict
from datetime import datetime


# ===========================================================================
#  CENTRAL STATUTES -- The Indian Parliament speaks first.
# ===========================================================================

class TransferOfPropertyAct1882:
    """
    Section 54: Sale is a transfer of ownership in exchange for a price paid,
    promised, or part-paid and part-promised.

    # NOTE: Price must be certain. An uncertain consideration voids the sale.
    #       Like faith, price cannot be vague.
    """
    @staticmethod
    def validate_sale_consideration(price: float) -> bool:
        return price > 0.0  # Zero rupees is a gift, not a sale.


class RegistrationAct1908:
    """
    Section 17: Instruments creating, declaring, assigning, limiting, or
    extinguishing any right, title, or interest in immovable property
    valued at one hundred rupees and upwards MUST be registered.

    # NOTE: An unregistered sale deed is not admissible as evidence of title.
    #       It exists, but it cannot speak in court. A mute document.
    """
    REQUIRED_VALUE_THRESHOLD: float = 100.0

    @classmethod
    def requires_registration(cls, value: float) -> bool:
        return value >= cls.REQUIRED_VALUE_THRESHOLD

    @staticmethod
    def verify_registered_at_sub_registrar(
        deed: Deed,
        sro_office: str
    ) -> bool:
        """
        A deed is not born until the Sub-Registrar stamps it.
        Bangalore Urban, Bangalore Rural, Mysuru, Belagavi --
        each office has its own index, its own delays, its own dust.
        """
        return deed.is_registered and deed.sro_jurisdiction == sro_office


class BenamiTransactionsProhibitionAct1988:
    """
    Section 3: No person shall enter into a benami transaction.

    # NOTE: The real owner hides behind a name. The law says: the veil is torn.
    #       Property held benami is liable to confiscation without compensation.
    """
    @staticmethod
    def is_benami(beneficial_owner: str, registered_owner: str) -> bool:
        """If the hands that paid are not the hands that hold, it is benami."""
        return beneficial_owner != registered_owner


class RERA2016:
    """
    The Real Estate (Regulation and Development) Act, 2016.

    Section 3: No promoter shall advertise, market, book, sell, offer for sale,
    or invite persons to purchase any apartment, plot, or building in a real
    estate project without registering the project with the Real Estate
    Regulatory Authority.

    # NOTE: Karnataka RERA Rules, 2017 apply here.
    #       The Authority sits in Bangalore. Project KH-RERA-XXXXXX.
    """
    AUTHORITY: str = "Karnataka Real Estate Regulatory Authority"

    @staticmethod
    def verify_project_registration(rera_id: Optional[str]) -> bool:
        """
        Without KH-RERA registration, the project is a ghost building.
        Buyers pour money into foundations that may never become floors.
        """
        return rera_id is not None and rera_id.startswith("KH-RERA-")

    @staticmethod
    def verify_escrow_account(funds_received: float, escrow_balance: float) -> bool:
        """
        Section 4(2)(l)(D): 70% of funds received must be deposited in
        a separate escrow account and utilised only for that project's costs.

        # FIXME: In practice, diversion is common. The code knows this.
        """
        return escrow_balance >= (funds_received * 0.70)


# ===========================================================================
#  KARNATAKA STATUTES -- The State speaks next. Its voice is local.
# ===========================================================================

class KarnatakaStampAct1957:
    """
    Article 20: Conveyance -- Sale of immovable property.

    Stamp duty in Karnataka is among the highest in India.
    The state takes its share before the buyer takes the key.

    # NOTE: Current rate (subject to amendment):
    #       5% of market value for general areas
    #       + 1% Registration fee
    #       + 2% Cess (in some municipal areas)
    #       + 10% surcharge on stamp duty
    #       = approximately 6.6% of guidance value.
    """
    STAMP_DUTY_RATE: float = 0.05
    REGISTRATION_FEE_RATE: float = 0.01
    SURCHARGE_RATE: float = 0.10  # On stamp duty only

    @classmethod
    def calculate_stamp_duty(cls, market_value: float) -> Dict[str, float]:
        stamp = market_value * cls.STAMP_DUTY_RATE
        reg_fee = market_value * cls.REGISTRATION_FEE_RATE
        surcharge = stamp * cls.SURCHARGE_RATE
        return {
            "stamp_duty": stamp,
            "registration_fee": reg_fee,
            "surcharge": surcharge,
            "total": stamp + reg_fee + surcharge,
        }

    @classmethod
    def is_stamp_sufficient(cls, market_value: float, paid: float) -> bool:
        required = cls.calculate_stamp_duty(market_value)["total"]
        return paid >= required


class KarnatakaLandRevenueAct1964:
    """
    Section 127: Mutation of names in the register of account No. 1 (Rahan).

    # NOTE: Mutation is not title. It is only revenue record.
    #       But without mutation, the new owner cannot pay tax in his own name.
    #       And without paying tax, the land aches in administrative limbo.
    """
    @staticmethod
    def verify_mutation(khata_holder: str, new_owner: str) -> bool:
        return khata_holder == new_owner


class KarnatakaPTCLAct1978:
    """
    Karnataka Scheduled Castes and Scheduled Tribes
    (Prohibition of Transfer of Certain Lands) Act, 1978.

    # WARNING: Land granted to SC/ST beneficiaries cannot be transferred.
    #          "Akram Sakram" -- regularisation -- is sometimes possible,
    #          but the shadow of this Act falls across many titles in Karnataka.
    #          A beautiful farm with a PTCL defect is a landmine in a garden.
    """
    @staticmethod
    def is_granted_land(land_type: str) -> bool:
        return land_type.lower() in ("sc grant", "st grant", "scheduled grant")

    @staticmethod
    def can_transfer(granted: bool, regularised: bool = False) -> bool:
        if not granted:
            return True
        # ERROR: Cannot transfer granted land unless regularised under Akram Sakram.
        #        ^^^ Type mismatch: legal title expected, got 'conditional future'.
        return regularised


# ===========================================================================
#  LAND USE -- Conversion is conversion. Agricultural to non-agricultural.
# ===========================================================================

class LandUseType(Enum):
    AGRICULTURAL = auto()
    RESIDENTIAL = auto()
    COMMERCIAL = auto()
    INDUSTRIAL = auto()
    MIXED_USE = auto()


class DCConversionRequired(Exception):
    """
    Section 95 of Karnataka Land Revenue Act, 1964:
    No agricultural land shall be used for non-agricultural purpose without
    obtaining permission from the Deputy Commissioner.

    # ERROR: DC conversion missing.
    #        ^^^ Semantic error: 'farmland' cannot be implicitly cast to 'homesite'
    #        Hint: Apply to the Deputy Commissioner's office. Attach Form 18.
    #              Wait. Then wait more.
    """
    pass


class KhataType(Enum):
    """
    A-Khata: Full regularisation. Clean title. Bankable. Mortgageable. The ideal.
    B-Khata: Recorded, but with deviations. Unauthorised construction,
             pending DC conversion, or revenue dues. Bank loans are difficult.
             Like a person known to the state but not fully accepted.

    # NOTE: The bifurcation is Bangalore's special wound. A gift to poets.
    """
    A = "A-Khata"  # The state embraces this property.
    B = "B-Khata"  # The state acknowledges but does not fully legitimise.


# ===========================================================================
#  CORE DATA STRUCTURES -- The atoms of property.
# ===========================================================================

@dataclass
class SurveyNumber:
    """Every field has a number. The state counts what the farmer sows."""
    number: str
    village: str
    hobli: str
    taluk: str
    district: str


@dataclass
class Property:
    """
    Immovable property under Indian law: land, benefits arising out of land,
    and things attached to the earth or permanently fastened to anything
    attached to the earth.

    # NOTE: Trees standing are immovable. Timber cut is movable.
    #       The same object changes legal nature by an act of severance.
    """
    survey: SurveyNumber
    extent_acres: float
    current_use: LandUseType
    dc_converted: bool = False
    is_scst_grant: bool = False
    khata: KhataType = KhataType.A
    guidance_value_per_sqft: float = 0.0
    market_value: float = 0.0
    building_plan_approved: bool = False


@dataclass
class Party:
    """A person before the law. The law does not ask if they dream."""
    name: str
    is_promoter: bool = False


@dataclass
class Deed:
    """
    The instrument of transfer. A document is not a deed unless it is
    executed and attested.

    # NOTE: Two witnesses minimum for sale deed under Indian Registration Act.
    #       Their names are witnesses to the witnessing. The chain of trust.
    """
    deed_number: str
    execution_date: datetime
    vendor: Party
    purchaser: Party
    property: Property
    sale_price: float
    witnesses: List[str] = field(default_factory=list)
    is_registered: bool = False
    sro_jurisdiction: str = ""
    stamp_duty_paid: float = 0.0
    rera_id: Optional[str] = None
    encumbrances: List[str] = field(default_factory=list)


# ===========================================================================
#  THE COMPILER -- Where law becomes executable.
# ===========================================================================

class CompilationError:
    """A defect in the legal source code. Rendered as an IDE-style diagnostic."""
    def __init__(self, file: str, line: int, severity: str, code: str, message: str):
        self.file = file
        self.line = line
        self.severity = severity  # ERROR, WARNING, INFO
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"{self.file}:{self.line}: {self.severity}: [{self.code}] {self.message}"


class LegalCompiler:
    """
    The compiler reads a deed as source and produces either:
        (a) a valid title -- clean output, or
        (b) a diagnostic log -- the errors that prevent legal existence.

    Each method is a statutory filter. The deed must pass all filters
    to be compiled into a marketable title.
    """

    def __init__(self):
        self.diagnostics: List[CompilationError] = []
        self.current_source_file = "deed.py"  # The fiction of a single file.
        self._line_counter = 0

    def _emit(self, severity: str, code: str, message: str):
        self._line_counter += 1
        err = CompilationError(
            file=self.current_source_file,
            line=self._line_counter,
            severity=severity,
            code=code,
            message=message,
        )
        self.diagnostics.append(err)

    def compile(self, deed: Deed) -> bool:
        """
        Compile a deed into a title.
        Returns True if the title is marketable (clean compile).
        Returns False if there are defects (compilation failed).
        """
        print("=" * 72)
        print("LEGAL COMPILER -- KARNATAKA EDITION")
        print(f"Compiling deed {deed.deed_number}...")
        print("=" * 72)
        print()

        # -- Phase 1: Lexical Analysis ---------------------------------------
        # Can the document even be read? Is it attested? Is it certain?
        self._check_attestation(deed)
        self._check_consideration(deed)

        # -- Phase 2: Semantic Analysis -- Statutory Compliance ----------------
        self._check_registration(deed)
        self._check_stamp_duty(deed)
        self._check_rera(deed)
        self._check_dc_conversion(deed)
        self._check_ptcl(deed)
        self._check_khata(deed)
        self._check_encumbrances(deed)
        self._check_benami(deed)

        # -- Phase 3: Linking -- Mutation & Revenue Records -------------------
        self._check_mutation_readiness(deed)

        # -- Build Report -----------------------------------------------------
        print()
        print("-" * 72)
        errors = [d for d in self.diagnostics if d.severity == "ERROR"]
        warnings = [d for d in self.diagnostics if d.severity == "WARNING"]
        infos = [d for d in self.diagnostics if d.severity == "INFO"]

        for d in self.diagnostics:
            print(d)

        print()
        print(f"Build complete: {len(errors)} error(s), {len(warnings)} warning(s), {len(infos)} note(s).")
        if errors:
            print("TITLE NOT MARKETABLE. Compilation failed.")
            print()
            print("# The property exists in the physical world,")
            print("# but it does not yet exist in the legal world.")
            print("# The code refuses to compile longing into ownership.")
            return False
        else:
            print("CLEAN BUILD. Title is marketable.")
            print()
            print("# The deed has passed through the statute-machinery.")
            print("# The state acknowledges: this land has an owner.")
            return True

    # -- Individual Statutory Checks ----------------------------------------

    def _check_attestation(self, deed: Deed):
        if len(deed.witnesses) < 2:
            self._emit(
                "ERROR", "REG1908-ATT",
                f"Sale deed requires minimum 2 witnesses. Found {len(deed.witnesses)}. "
                "Unattested deed is inadmissible as evidence of transfer."
            )
        else:
            self._emit("INFO", "REG1908-OK", f"Attested by {len(deed.witnesses)} witness(es).")

    def _check_consideration(self, deed: Deed):
        if not TransferOfPropertyAct1882.validate_sale_consideration(deed.sale_price):
            self._emit(
                "ERROR", "TOP1882-SALE",
                "Sale consideration is zero or unspecified. "
                "Section 54 requires a price -- paid, promised, or part-paid and part-promised."
            )
        else:
            self._emit("INFO", "TOP1882-OK", f"Consideration of INR {deed.sale_price:,.2f} is valid.")

    def _check_registration(self, deed: Deed):
        if not deed.is_registered:
            self._emit(
                "ERROR", "REG1908-NOREG",
                f"Deed {deed.deed_number} is UNREGISTERED. "
                "Section 17: Sale of immovable property > INR 100 must be registered. "
                "An unregistered deed is a shadow -- it exists but cannot speak in court."
            )
            # =================================================================
            #  ERROR: registration is the birth certificate of a deed.
            #         Without it, the document is stillborn.
            #         ^^^ Semantic error: deed.registered is None
            #         Hint: Visit Sub-Registrar Office. Pay stamp duty. Wait.
            #               The state bureaucracy is the compiler. You cannot bypass it.
            # =================================================================
        else:
            self._emit("INFO", "REG1908-OK", f"Registered at SRO: {deed.sro_jurisdiction}")

    def _check_stamp_duty(self, deed: Deed):
        required = KarnatakaStampAct1957.calculate_stamp_duty(deed.property.market_value)["total"]
        if not KarnatakaStampAct1957.is_stamp_sufficient(deed.property.market_value, deed.stamp_duty_paid):
            deficit = required - deed.stamp_duty_paid
            self._emit(
                "ERROR", "KSA1957-STAMP",
                f"Stamp duty deficit of INR {deficit:,.2f}. "
                f"Paid INR {deed.stamp_duty_paid:,.2f}, required INR {required:,.2f}. "
                "Under-stamped instrument is inadmissible and liable to impounding."
            )
        else:
            self._emit("INFO", "KSA1957-OK", f"Stamp duty satisfied (INR {deed.stamp_duty_paid:,.2f}).")

    def _check_rera(self, deed: Deed):
        if deed.vendor.is_promoter:
            if not RERA2016.verify_project_registration(deed.rera_id):
                self._emit(
                    "ERROR", "RERA2016-NOREG",
                    f"Promoter sale without RERA registration. "
                    f"Project ID '{deed.rera_id}' is not a valid KH-RERA identifier. "
                    "Section 3: No promoter shall sell without registering the project."
                )
            else:
                self._emit("INFO", "RERA2016-OK", f"Project registered under {deed.rera_id}.")
        else:
            self._emit("INFO", "RERA2016-NA", "Seller is not a promoter. RERA check not applicable.")

    def _check_dc_conversion(self, deed: Deed):
        prop = deed.property
        if prop.current_use != LandUseType.AGRICULTURAL and not prop.dc_converted:
            self._emit(
                "ERROR", "KLR1964-DC",
                f"Property survey {prop.survey.number} is used for {prop.current_use.name} "
                f"but lacks DC conversion from agricultural use. "
                "Section 95 Karnataka Land Revenue Act: permission of Deputy Commissioner required."
            )
            # =================================================================
            #  WARNING: DC conversion is the rite of passage for farmland.
            #           Without it, the land dreams of being a home
            #           but wakes up still a field.
            #           ^^^ TypeError: cannot convert 'AgriculturalLand' to 'ResidentialPlot'
            #           without explicit DCConversion(apply=True, bribe=False, wait=forever)
            # =================================================================
        elif prop.current_use != LandUseType.AGRICULTURAL and prop.dc_converted:
            self._emit("INFO", "KLR1964-DC-OK", "DC conversion certificate is on file.")

    def _check_ptcl(self, deed: Deed):
        prop = deed.property
        if prop.is_scst_grant:
            self._emit(
                "ERROR", "PTCL1978-GRANT",
                f"Property survey {prop.survey.number} is SC/ST granted land. "
                "Karnataka PTCL Act 1978 prohibits transfer. "
                "Title is void ab initio -- void from the beginning, as if it never was."
            )
            # =================================================================
            #  FATAL ERROR: PTCL violation detected.
            #               ^^^ This land was given to a scheduled caste family
            #                   by the state as reparation. The state remembers.
            #                   The transfer is not merely defective. It is dead.
            #                   There is no fix. There is only confiscation.
            # =================================================================

    def _check_khata(self, deed: Deed):
        if deed.property.khata == KhataType.B:
            self._emit(
                "WARNING", "BBMP-KHATA-B",
                "Property holds B-Khata status. Revenue records show unauthorised "
                "construction or pending compliance. Banks may refuse mortgage. "
                "Marketability is impaired. Consider Khata amalgamation/regularisation."
            )
            # =================================================================
            #  WARNING: B-Khata is the liminal space of Bangalore property.
            #           Not illegal, not fully legal. A twilight title.
            #           ^^^ DeprecationWarning: KhataType.B is deprecated;
            #               use KhataType.A in future transactions.
            #               Regularisation path: Betterment Charge + Sakrama Scheme.
            # =================================================================
        else:
            self._emit("INFO", "BBMP-OK", "A-Khata: clean revenue record.")

    def _check_encumbrances(self, deed: Deed):
        if deed.encumbrances:
            for enc in deed.encumbrances:
                self._emit(
                    "WARNING", "EC-ENCUMBRANCE",
                    f"Encumbrance on title: {enc}. "
                    "EC shows prior mortgage/charge. Marketability subject to discharge."
                )
        else:
            self._emit("INFO", "EC-OK", "Encumbrance Certificate is clear for 30 years.")

    def _check_benami(self, deed: Deed):
        if BenamiTransactionsProhibitionAct1988.is_benami(
            beneficial_owner=deed.purchaser.name,
            registered_owner=deed.vendor.name
        ):
            # In a real transaction, we'd need the beneficial owner declared.
            # Here we only check if vendor and purchaser are the same entity
            # which would be suspicious -- but truly benami needs external facts.
            pass  # Left as conceptual marker. True benami requires investigation.

    def _check_mutation_readiness(self, deed: Deed):
        if deed.is_registered:
            self._emit(
                "INFO", "KLR1964-MUT",
                f"Deed registered. Proceed to mutation application at "
                f"{deed.property.survey.taluk} Taluk office. Form 21. "
                "Mutation is not title, but it is the tax-face of ownership."
            )


# ===========================================================================
#  SAMPLE TRANSACTION -- A defective deed. The art is in the failure.
# ===========================================================================

def main():
    """
    Here is a property transaction. It is beautiful in its defects.
    Like a body with scars, it tells the story of what the law permits
    and what it forbids.

    # NOTE: This deed is INTENTIONALLY defective. Running the compiler
    #       will produce errors. The errors ARE the art.
    #       Each error is a verse in the poem of property law.
    """

    survey = SurveyNumber(
        number="45/2A",
        village="Kannur",
        hobli="Hesaraghatta",
        taluk="Bangalore North",
        district="Bangalore Urban",
    )

    the_land = Property(
        survey=survey,
        extent_acres=1.25,
        current_use=LandUseType.RESIDENTIAL,  # But no DC conversion!
        dc_converted=False,                    # ^^^ ERROR here
        is_scst_grant=True,                    # ^^^ FATAL ERROR here
        khata=KhataType.B,                     # ^^^ WARNING here
        guidance_value_per_sqft=5200.0,
        market_value=6_500_000.0,
        building_plan_approved=False,
    )

    # The vendor is a promoter. But there is no RERA ID.
    # ^^^ ERROR: promote() called without project registration.
    #            The building rises in the ads but not in the authority's ledger.
    vendor = Party(name="Green Meadows Developers Pvt Ltd", is_promoter=True)

    purchaser = Party(name="Ramesh K.")

    defective_deed = Deed(
        deed_number="BDL-2024-88421",
        execution_date=datetime(2024, 3, 15),
        vendor=vendor,
        purchaser=purchaser,
        property=the_land,
        sale_price=6_500_000.0,
        witnesses=["Suresh N."],  # Only one witness. Need two.
                                  # ^^^ ERROR: witness list has insufficient elements.
        is_registered=False,      # Not registered at Sub-Registrar.
                                  # ^^^ ERROR: deed.registered flag is False.
        sro_jurisdiction="",
        stamp_duty_paid=150_000.0,  # Far below the ~INR 429,000 required.
                                    # ^^^ ERROR: stamp duty insufficient.
        rera_id=None,               # Promoter without RERA.
                                    # ^^^ ERROR: missing required parameter 'rera_id'.
        encumbrances=["Mortgage to Karnataka Bank, 2022, INR 4,000,000"],
                                    # ^^^ WARNING: prior charge exists.
    )

    compiler = LegalCompiler()
    compiler.compile(defective_deed)

    # =======================================================================
    #  FINAL REMARK: This program does not merely simulate law.
    #                It performs law. The exceptions are real.
    #                The void is real. The B-Khata is real.
    #                When you run it, you see what the state sees:
    #                a document that wants to be property but is not yet.
    #
    #  To make it compile cleanly, fix the errors above:
    #    - Add a second witness.
    #    - Register at SRO Bangalore North.
    #    - Pay full stamp duty (INR 429,000+).
    #    - Obtain DC conversion.
    #    - Verify this is NOT granted land (or obtain Akram Sakram).
    #    - Upgrade to A-Khata.
    #    - Obtain RERA registration (KH-RERA-XXXXX).
    #    - Discharge the Karnataka Bank mortgage.
    #
    #  Until then, the land is a poem that the compiler refuses to parse.
    # =======================================================================


if __name__ == "__main__":
    main()

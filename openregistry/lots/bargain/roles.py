# -*- coding: utf-8 -*-

from schematics.transforms import blacklist, whitelist
from openregistry.lots.core.models import (
    plain_role,
    listing_role
)
from openregistry.lots.core.models import (
    schematics_default_role,
    lots_embedded_role
)

from openregistry.lots.bargain.constants import DEFAULT_PROCUREMENT_TYPE


item_create_role = blacklist('id')
item_edit_role = blacklist('id')
item_view_role = (schematics_default_role + blacklist())


item_roles = {
    'create': item_create_role,
    'edit': item_edit_role,
    'view': item_view_role,
}

auction_create_role = blacklist('id', 'status', 'auctionID', 'relatedProcessID', 'procurementMethodType')
auction_common_edit_role = blacklist(
    'id', 'auctionID', 'procurementMethodType',
    'status', 'relatedProcessID'
)
auction_view_role = (schematics_default_role + blacklist())
edit_auction = auction_common_edit_role


auction_roles = {
    'create': auction_create_role,
    'edit': auction_common_edit_role,
    'view': auction_view_role,
    'edit_{}'.format(DEFAULT_PROCUREMENT_TYPE): edit_auction,
    'convoy': whitelist('status'),
    'concierge': whitelist('status', 'auctionID', 'relatedProcessID')
}


lot_create_role = (whitelist(
    'status', 'assets', 'lotType', 'lotIdentifier', 'mode', 'sandboxParameters',
    'decisions', 'relatedProcesses')
)
lot_edit_role = (blacklist(
    'owner_token', 'owner', '_attachments', 'contracts',
    'revisions', 'date', 'dateModified', 'documents', 'auctions', 'relatedProcesses', 'lotType',
    'lotID', 'mode', 'doc_id', 'decisions') + lots_embedded_role)
view_role = (blacklist('owner_token', '_attachments', 'revisions') + lots_embedded_role)

Administrator_role = whitelist('status', 'mode')
concierge_role = (blacklist(
    'owner_token', 'owner', '_attachments', 'revisions', 'date', 'dateModified',
    'lotID', 'mode', 'doc_id') + lots_embedded_role)

decision_roles = {
    'view': (schematics_default_role + blacklist()),
    'create': blacklist('decisionOf', 'relatedItem'),
    'edit': blacklist('id', 'decisionOf', 'relatedItem')
}

contracts_roles = {
    'view': (schematics_default_role + blacklist()),
    'caravan': blacklist('id', 'type'),
    'convoy': blacklist('id', 'type'),
}

concierge_edit_role = whitelist(
    'status', 'decisions', 'title', 'title_ru', 'title_en',
    'lotCustodian', 'description', 'description_ru', 'description_en',
    'lotHolder', 'items'
)

lot_roles = {
    'create': lot_create_role,
    'plain': plain_role,
    'edit': lot_edit_role,
    'view': view_role,
    'listing': listing_role,
    'default': schematics_default_role,
    'Administrator': Administrator_role,
    # Draft role
    'draft': view_role,
    'edit_draft': whitelist('status'),
    # Composing role
    'composing': view_role,
    'edit_composing': whitelist('status'),
    'verification': view_role,
    'edit_verification': whitelist(),
    # Pending role
    'pending': view_role,
    'edit_pending': lot_edit_role,
    # Pending.deleted role
    'pending.deleted': view_role,
    'edit_pending.deleted': whitelist(),
    # Deleted role
    'deleted': view_role,
    'edit_deleted': whitelist(),
    # Active.salable role
    'active.salable': view_role,
    'edit_active.salable': whitelist(),
    # pending.dissolution role
    'pending.dissolution': view_role,
    'edit_pending.dissolution': whitelist(),
    # Dissolved role
    'dissolved': view_role,
    'edit_dissolved': whitelist(),
    # Active.awaiting role
    'active.awaiting': view_role,
    'edit_active.awaiting': whitelist(),
    # Active.auction role
    'active.auction': view_role,
    'edit_active.auction': whitelist(),
    # Active.contracting role
    'active.contracting': view_role,
    'edit_active.contracting': whitelist(),
    # pending.sold role
    'pending.sold': view_role,
    'edit.pending.sold': whitelist(),
    # Sold role
    'sold': view_role,
    'edit.sold': whitelist(),
    'invalid': view_role,
    'edit.invalid': whitelist(),
    'concierge': concierge_edit_role,
    'chronograph': whitelist(),
    'caravan': whitelist(),
    'convoy': whitelist()
}

from __future__ import absolute_import
import weakref
from defcon.tools.notifications import NotificationCenter
import pickle

class BaseObject(object):

    """
    The base object in defcon from which all other objects should be derived.

    **This object posts the following notifications:**

<<<<<<< HEAD
    ====================
    Name
    ====================
    BaseObject.Changed
    BaseObject.BeginUndo
    BaseObject.EndUndo
    BaseObject.BeginRedo
    BaseObject.EndRedo
    ====================
=======
    ====================  ====
    Name                  Note
    ====================  ====
    BaseObject.Changed    Posted when the *dirty* attribute is set.
    BaseObject.BeginUndo  Posted when an undo begins.
    BaseObject.EndUndo    Posted when an undo ends.
    BaseObject.BeginRedo  Posted when a redo begins.
    BaseObject.EndRedo    Posted when a redo ends.
    ====================  ====
>>>>>>> typesupply/master

    Keep in mind that subclasses will not post these same notifications.

    Subclasses must override the following attributes:

    +-------------------------+--------------------------------------------------+
    | Name                    | Notes                                            |
    +=========================+==================================================+
    | changeNotificationName  | This must be a string unique to the class        |
    |                         | indicating the name of the notification          |
    |                         | to be posted when the dirty attribute is set.    |
    +-------------------------+--------------------------------------------------+
    | representationFactories | This must be a dictionary that is shared across  |
    |                         | *all* instances of the class.                    |
    +-------------------------+--------------------------------------------------+
    """

    changeNotificationName = "BaseObject.Changed"
    beginUndoNotificationName = "BaseObject.BeginUndo"
    endUndoNotificationName = "BaseObject.EndUndo"
    beginRedoNotificationName = "BaseObject.BeginRedo"
    endRedoNotificationName = "BaseObject.EndRedo"
<<<<<<< HEAD
    representationFactories = None
=======
>>>>>>> typesupply/master

    def __init__(self):
        self._init()

    def _init(self):
        self._dispatcher = None
        self._dataOnDisk = None
        self._dataOnDiskTimeStamp = None
        self._undoManager = None
<<<<<<< HEAD
        self._representations = {}
=======
        # handle the old _notificationName attribute
        if hasattr(self, "_notificationName"):
            from warnings import warn
            warn(
                "_notificationName has been deprecated. Use changeNotificationName instead.",
                DeprecationWarning
            )
            self.changeNotificationName = self._notificationName
        self._notificationName = self.changeNotificationName

    # ------
    # Parent
    # ------
>>>>>>> typesupply/master

    def __del__(self):
        self.endSelfNotificationObservation()

    # ------
    # Parent
    # ------

    def getParent(self):
        raise NotImplementedError

    # -------------
    # Notifications
    # -------------

    # -------------
    # Notifications
    # -------------

    def _get_dispatcher(self):
        if self._dispatcher is not None:
            return self._dispatcher()
        else:
            try:
                dispatcher = self.font.dispatcher
                self._dispatcher = weakref.ref(dispatcher)
            except AttributeError:
                dispatcher = None
        return dispatcher

    dispatcher = property(_get_dispatcher, doc="The :class:`defcon.tools.notifications.NotificationCenter` assigned to the parent of this object.")

    def addObserver(self, observer, methodName, notification):
        """
        Add an observer to this object's notification dispatcher.

        * **observer** An object that can be referenced with weakref.
        * **methodName** A string representing the method to be called
          when the notification is posted.
        * **notification** The notification that the observer should
          be notified of.

        The method that will be called as a result of the action
        must accept a single *notification* argument. This will
        be a :class:`defcon.tools.notifications.Notification` object.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.addObserver(observer=observer, methodName=methodName,
                notification=notification, observable=anObject)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            self.dispatcher.addObserver(observer=observer, methodName=methodName,
                notification=notification, observable=self)

    def removeObserver(self, observer, notification):
        """
        Remove an observer from this object's notification dispatcher.

        * **observer** A registered object.
        * **notification** The notification that the observer was registered
          to be notified of.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.removeObserver(observer=observer,
                notification=notification, observable=anObject)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            self.dispatcher.removeObserver(observer=observer, notification=notification, observable=self)

    def hasObserver(self, observer, notification):
        """
        Returns a boolean indicating is the **observer** is registered for **notification**.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.hasObserver(observer=observer,
                notification=notification, observable=anObject)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            return self.dispatcher.hasObserver(observer=observer, notification=notification, observable=self)
        return False

    def holdNotifications(self, notification=None):
        """
        Hold this object's notifications until told to release them.

        * **notification** The specific notification to hold. This is optional.
          If no *notification* is given, all notifications will be held.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.holdNotifications(
                observable=anObject, notification=notification)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.holdNotifications(observable=self, notification=notification)

    def releaseHeldNotifications(self, notification=None):
        """
        Release this object's held notifications.

        * **notification** The specific notification to hold. This is optional.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.releaseHeldNotifications(
                observable=anObject, notification=notification)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.releaseHeldNotifications(observable=self, notification=notification)

    def disableNotifications(self, notification=None, observer=None):
        """
        Disable this object's notifications until told to resume them.

        * **notification** The specific notification to disable. This is optional.
          If no *notification* is given, all notifications will be disabled.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.disableNotifications(
                observable=anObject, notification=notification, observer=observer)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.disableNotifications(observable=self, notification=notification, observer=observer)

    def enableNotifications(self, notification=None, observer=None):
        """
        Enable this object's notifications.

        * **notification** The specific notification to enable. This is optional.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.enableNotifications(
                observable=anObject, notification=notification, observer=observer)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.enableNotifications(observable=self, notification=notification, observer=observer)

    def postNotification(self, notification, data=None):
        """
        Post a **notification** through this object's notification dispatcher.

            * **notification** The name of the notification.
            * **data** Arbitrary data that will be stored in the :class:`Notification` object.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.postNotification(
                notification=notification, observable=anObject, data=data)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.postNotification(notification=notification, observable=self, data=data)

    # ------------------------
    # Notification Observation
    # ------------------------

    def beginSelfNotificationObservation(self):
        self.addObserver(self, "selfNotificationCallback", notification=None)

    def endSelfNotificationObservation(self):
        self.removeObserver(self, notification=None)
        self._dispatcher = None

    def selfNotificationCallback(self, notification):
        self._destroyRepresentationsForNotification(notification)

    # ----
    # Undo
    # ----

    # manager

    def _get_undoManager(self):
        return self._undoManager

    def _set_undoManager(self, manager):
        self._undoManager = manager

    undoManager = property(_get_undoManager, _set_undoManager,
                           doc="The undo manager assigned to this object.")

    # state registration

    def prepareUndo(self, *args, **kwargs):
        self.undoManager.prepareTarget(*args, **kwargs)

    # undo

    def canUndo(self):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.canUndo()

    def getUndoTitle(self, index=None):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        if index is None:
            index = -1
        return manager.getUndoTitle(index)

    def _undo(self, index):
        if index is None:
            index = -1
        self.undoManager.undo(index)

    def undo(self, index=None):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        dispatcher = self._dispatcher
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.beginUndoNotificationName, observable=self)
        self._undo(index)
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.endUndoNotificationName, observable=self)

    # redo

    def canRedo(self):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.canRedo()

    def getRedoTitle(self, index=None):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        if index is None:
            index = 0
        return manager.getRedoTitle(index)

    def _redo(self, index):
        if index is None:
            index = 0
        self.undoManager.redo(index)

    def redo(self, index=None):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        dispatcher = self._dispatcher
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.beginRedoNotificationName, observable=self)
        self._redo(index)
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.endRedoNotificationName, observable=self)

    # ---------------
    # Representations
    # ---------------

    def getRepresentation(self, name, **kwargs):
        """
        Get a representation. **name** must be a registered
        representation name. **\*\*kwargs** will be passed
        to the appropriate representation factory.
        """
        if name not in self._representations:
            self._representations[name] = {}
        representations = self._representations[name]
        subKey = self._makeRepresentationSubKey(**kwargs)
        if subKey not in representations:
            factory = self.representationFactories[name]
            representation = factory["factory"](self, **kwargs)
            representations[subKey] = representation
        return representations[subKey]

    def destroyRepresentation(self, name, **kwargs):
        """
        Destroy the stored representation for **name**
        and **\*\*kwargs**. If no **kwargs** are given,
        any representation with **name** will be destroyed
        regardless of the **kwargs** passed when the
        representation was created.
        """
        if name not in self._representations:
            return
        if not kwargs:
            del self._representations[name]
        else:
            representations = self._representations[name]
            subKey = self._makeRepresentationSubKey(**kwargs)
            if subKey in representations:
                del self._representations[name][subKey]

    def destroyAllRepresentations(self, notification=None):
        """
        Destroy all representations.
        """
        self._representations.clear()

    def _destroyRepresentationsForNotification(self, notification):
        notificationName = notification.name
        for name, dataDict in self.representationFactories.items():
            if notificationName in dataDict["destructiveNotifications"]:
                self.destroyRepresentation(name)

    def representationKeys(self):
        """
        Get a list of all representation keys that are
        currently cached.
        """
        representations = []
        for name, subDict in self._representations.items():
            for subKey in subDict.keys():
                kwargs = {}
                if subKey is not None:
                    for k, v in subKey:
                        kwargs[k] = v
                representations.append((name, kwargs))
        return representations

    def hasCachedRepresentation(self, name, **kwargs):
        """
        Returns a boolean indicating if a representation for
        **name** and **\*\*kwargs** is cached in the object.
        """
        if name not in self._representations:
            return False
        subKey = self._makeRepresentationSubKey(**kwargs)
        return subKey in self._representations[name]

    def _makeRepresentationSubKey(self, **kwargs):
        if kwargs:
            key = sorted(kwargs.items())
            key = tuple(key)
        else:
            key = None
        return key

    # -----
    # Dirty
    # -----

    def holdNotifications(self, notification=None):
        """
        Hold this object's notifications until told to release them.

        * **notification** The specific notification to hold. This is optional.
          If no *notification* is given, all notifications will be held.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.holdNotifications(
                observable=anObject, notification=notification)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.holdNotifications(observable=self, notification=notification)

    def releaseHeldNotifications(self, notification=None):
        """
        Release this object's held notifications.

        * **notification** The specific notification to hold. This is optional.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.releaseHeldNotifications(
                observable=anObject, notification=notification)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.releaseHeldNotifications(observable=self, notification=notification)

    def disableNotifications(self, notification=None, observer=None):
        """
        Disable this object's notifications until told to resume them.

        * **notification** The specific notification to disable. This is optional.
          If no *notification* is given, all notifications will be disabled.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.disableNotifications(
                observable=anObject, notification=notification, observer=observer)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.disableNotifications(observable=self, notification=notification, observer=observer)

    def enableNotifications(self, notification=None, observer=None):
        """
        Enable this object's notifications.

        * **notification** The specific notification to enable. This is optional.

        This is a convenience method that does the same thing as::

            dispatcher = anObject.dispatcher
            dispatcher.enableNotifications(
                observable=anObject, notification=notification, observer=observer)
        """
        dispatcher = self.dispatcher
        if dispatcher is not None:
            dispatcher.enableNotifications(observable=self, notification=notification, observer=observer)

    # -----
    # Dirty
    # -----

    def _set_dirty(self, value):
        self._dirty = value
<<<<<<< HEAD
        dispatcher = self.dispatcher
        if dispatcher is not None:
            self.postNotification(self.changeNotificationName)
=======
        if self._dispatcher is not None:
            self.dispatcher.postNotification(notification=self.changeNotificationName, observable=self)
>>>>>>> typesupply/master

    def _get_dirty(self):
        return self._dirty

    dirty = property(_get_dirty, _set_dirty, doc="The dirty state of the object. True if the object has been changed. False if not. Setting this to True will cause the base changed notification to be posted. The object will automatically maintain this attribute and update it as you change the object.")

<<<<<<< HEAD
    # -----------------------------
    # Serialization/Deserialization
    # -----------------------------
=======
    # ----
    # Undo
    # ----

    # manager

    def _get_undoManager(self):
        return self._undoManager

    def _set_undoManager(self, manager):
        self._undoManager = manager
        manager.setObject(self)

    undoManager = property(_get_undoManager, _set_undoManager, doc="The undo manager assigned to this object.")

    # state registration

    def prepareUndo(self, title=None):
        self.undoManager.prepareTarget(title=title)

    # undo

    def canUndo(self):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.canUndo()

    def getUndoTitle(self, index=-1):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.getUndoTitle(index)

    def getUndoTitles(self):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.getUndoTitles()

    def undo(self, index=-1):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        dispatcher = self._dispatcher
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.beginUndoNotificationName, observable=self)
        manager.undo(index)
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.endUndoNotificationName, observable=self)

    # redo

    def canRedo(self):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.canRedo()

    def getRedoTitle(self, index=0):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.getRedoTitle(index)

    def getRedoTitles(self):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        return manager.getRedoTitles()

    def redo(self, index=0):
        manager = self.undoManager
        if manager is None:
            raise NotImplementedError
        dispatcher = self._dispatcher
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.beginRedoNotificationName, observable=self)
        manager.undo(index)
        if dispatcher is not None:
            self.dispatcher.postNotification(notification=self.endRedoNotificationName, observable=self)

    # serialization

    def serializeForUndo(self, pack=True):
        from cPickle import dumps
        import zlib
        # make the data dict
        data = dict(
            serializedData=self.getDataToSerializeForUndo(),
            customData=self.getCustomDataToSerializeForUndo()
        )
        if pack:
            # pickle
            data = dumps(data, 0)
            # compress
            data = zlib.compress(data, 9)
        return dict(packed=pack, data=data)

    def getDataToSerializeForUndo(self):
        raise NotImplementedError

    def getCustomDataToSerializeForUndo(self):
        return None

    # deserealization

    def deserializeFromUndo(self, data):
        from cPickle import loads
        import zlib
        packed = data["packed"]
        data = data["data"]
        if packed:
            # decompress
            data = zlib.decompress(data)
            # unpickle
            data = loads(data)
        # hold notifications
        self.holdNotifications()
        # deserialize basic data
        self.loadDeserializedDataFromUndo(data["serializedData"])
        # deserialize custom data
        self.loadDeserializedCustomDataFromUndo(data["customData"])
        # release held notifications
        self.releaseHeldNotifications()

    def loadDeserializedDataFromUndo(self, data):
        raise NotImplementedError

    def loadDeserializedCustomDataFromUndo(self, data):
        pass

>>>>>>> typesupply/master

    def serialize(self, dumpFunc=None, whitelist=None, blacklist=None):
        data = self.getDataForSerialization(whitelist=whitelist, blacklist=blacklist)

        dump = dumpFunc if dumpFunc is not None else pickle.dumps
        return dump(data)

    def deserialize(self, data, loadFunc=None):
        load = loadFunc if loadFunc is not None else pickle.loads
        self.setDataFromSerialization(load(data))

    def getDataForSerialization(self, **kwargs):
        """
        Return a dict of data that can be pickled.
        """
        return {}

    def setDataFromSerialization(self, data):
        """
        Restore state from the provided data-dict.
        """
        pass

    def _serialize(self, getters, whitelist=None, blacklist=None, **kwargs):
        """ A helper function for the defcon objects.

        Return a dict where the keys are the keys in getters and the values
        are the results of the getter functions

        getters is a list of tuples:
        [
            (:str:key, :callable:getter_function)
        ]

        if a whitelist is not None: the key must be in whitelist
        if a blacklist is not None: the key must not be in blacklist
        """
        data = {}
        for key, getter in getters:
            if whitelist is not None and key not in whitelist:
                continue
            if blacklist is not None and key in blacklist:
                continue
            data[key] = getter(key)
        return data




class BaseDictObject(dict, BaseObject):

    """
    A subclass of BaseObject that implements a dict API. Any changes
    to the contents of the object will cause the dirty attribute
    to be set to True.
    """

    setItemNotificationName = None
    deleteItemNotificationName = None
    clearNotificationName = None
    updateNotificationName = None

    def __init__(self):
        super(BaseDictObject, self).__init__()
        self._init()
        self._dirty = False

    def _get_dict(self):
        from warnings import warn
        warn(
            "BaseDictObject is now a dict and _dict is gone.",
            DeprecationWarning
        )
        return self

    _dict = property(_get_dict)

    def __hash__(self):
        return id(self)

    def __setitem__(self, key, value):
        oldValue = None
        if key in self:
            oldValue = self[key]
            if value is not None and oldValue == value:
                # don't do this if the value is None since some
                # subclasses establish their keys at startup with
                # self[key] = None
                return
        super(BaseDictObject, self).__setitem__(key, value)
        if self.setItemNotificationName is not None:
            self.postNotification(self.setItemNotificationName, data=dict(key=key, oldValue=oldValue, newValue=value))
        self.dirty = True

    def __delitem__(self, key):
        super(BaseDictObject, self).__delitem__(key)
        if self.deleteItemNotificationName is not None:
            self.postNotification(self.deleteItemNotificationName, data=dict(key=key))
        self.dirty = True

<<<<<<< HEAD
    def __deepcopy__(self, memo={}):
        import copy
        obj = self.__class__()
        for k, v in self.items():
            k = copy.deepcopy(k)
            v = copy.deepcopy(v)
            obj[k] = v
        return obj
=======
    def __copy__(self):
        import copy
        obj = self.__class__()
        obj.update(copy.copy(self._dict))
        return obj

    def __deepcopy__(self, memo={}):
        import copy
        obj = self.__class__()
        obj.update(copy.deepcopy(self._dict, memo))
        return obj

    def get(self, key, default=None):
        return self._dict.get(key, default)
>>>>>>> typesupply/master

    def clear(self):
        if not len(self):
            return
        super(BaseDictObject, self).clear()
        if self.clearNotificationName is not None:
            self.postNotification(self.clearNotificationName)
        self.dirty = True

    def update(self, other):
        super(BaseDictObject, self).update(other)
        if self.updateNotificationName is not None:
            self.postNotification(self.updateNotificationName)
        self.dirty = True

    # -----------------------------
    # Serialization/Deserialization
    # -----------------------------

    def getDataForSerialization(self, **kwargs):
        from copy import deepcopy

        deep_get = lambda k: deepcopy(self[k])

<<<<<<< HEAD
        getters = []
        for k in self.keys():
            k = deepcopy(k)  # needed?
            getters.append((k, deep_get))
=======
    # ----
    # Undo
    # ----

    def getDataToSerializeForUndo(self):
        return self._dict

    def loadDeserializedDataFromUndo(self, data):
        self.update(data)

>>>>>>> typesupply/master

        return self._serialize(getters, **kwargs)

    def setDataFromSerialization(self, data):
        self.clear()
        self.update(data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

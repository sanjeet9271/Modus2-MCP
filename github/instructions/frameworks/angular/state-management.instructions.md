# Angular State Management for Modus Components

> **Important Note**: These instructions only **apply to** Angular Projects.
> **LEAD LEVEL GUIDANCE**: This document provides Angular-specific patterns for state management when using Modus components.

## Overview

State management is a critical aspect of Angular applications using Modus components. This document outlines recommended approaches for managing state across various complexity levels.

## State Management Options

### 1. Component State

For simple components with isolated state, use local component state:

```typescript
@Component({
  selector: 'app-simple-state',
  template: `
    <div>
      <modus-button (buttonClick)="incrementCounter()">Increment</modus-button>
      <p>Count: {{ counter }}</p>
    </div>
  `
})
export class SimpleStateComponent {
  counter = 0;
  
  incrementCounter() {
    this.counter++;
  }
}
```

### 2. Service-based State Management

For sharing state between components in the same feature:

```typescript
// counter.service.ts
@Injectable({
  providedIn: 'root'
})
export class CounterService {
  private counterSubject = new BehaviorSubject<number>(0);
  counter$ = this.counterSubject.asObservable();
  
  incrementCounter() {
    this.counterSubject.next(this.counterSubject.value + 1);
  }
  
  resetCounter() {
    this.counterSubject.next(0);
  }
}

// counter.component.ts
@Component({
  selector: 'app-counter',
  template: `
    <div>
      <modus-button #incrementButton>Increment</modus-button>
      <modus-button #resetButton>Reset</modus-button>
      <p>Count: {{ counter$ | async }}</p>
    </div>
  `
})
export class CounterComponent implements AfterViewInit, OnDestroy {
  @ViewChild('incrementButton') incrementButtonRef!: ElementRef;
  @ViewChild('resetButton') resetButtonRef!: ElementRef;
  
  counter$ = this.counterService.counter$;
  
  constructor(private counterService: CounterService) {}
  
  ngAfterViewInit() {
    if (this.incrementButtonRef?.nativeElement) {
      this.incrementButtonRef.nativeElement.addEventListener('buttonClick', this.increment);
    }
    
    if (this.resetButtonRef?.nativeElement) {
      this.resetButtonRef.nativeElement.addEventListener('buttonClick', this.reset);
    }
  }
  
  ngOnDestroy() {
    if (this.incrementButtonRef?.nativeElement) {
      this.incrementButtonRef.nativeElement.removeEventListener('buttonClick', this.increment);
    }
    
    if (this.resetButtonRef?.nativeElement) {
      this.resetButtonRef.nativeElement.removeEventListener('buttonClick', this.reset);
    }
  }
  
  increment = () => {
    this.counterService.incrementCounter();
  }
  
  reset = () => {
    this.counterService.resetCounter();
  }
}
```

### 3. NgRx for Complex Applications

For large applications with complex state requirements:

```typescript
// counter.actions.ts
export const increment = createAction('[Counter] Increment');
export const decrement = createAction('[Counter] Decrement');
export const reset = createAction('[Counter] Reset');

// counter.reducer.ts
export interface CounterState {
  count: number;
}

export const initialState: CounterState = {
  count: 0
};

export const counterReducer = createReducer(
  initialState,
  on(increment, state => ({ ...state, count: state.count + 1 })),
  on(decrement, state => ({ ...state, count: state.count - 1 })),
  on(reset, state => ({ ...state, count: 0 }))
);

// counter.selectors.ts
export const selectCount = (state: { counter: CounterState }) => state.counter.count;

// counter.component.ts
@Component({
  selector: 'app-counter',
  template: `
    <div>
      <modus-button #incrementButton>Increment</modus-button>
      <modus-button #decrementButton>Decrement</modus-button>
      <modus-button #resetButton>Reset</modus-button>
      <p>Count: {{ count$ | async }}</p>
    </div>
  `
})
export class CounterComponent implements AfterViewInit, OnDestroy {
  @ViewChild('incrementButton') incrementButtonRef!: ElementRef;
  @ViewChild('decrementButton') decrementButtonRef!: ElementRef;
  @ViewChild('resetButton') resetButtonRef!: ElementRef;
  
  count$ = this.store.select(selectCount);
  
  constructor(private store: Store) {}
  
  ngAfterViewInit() {
    if (this.incrementButtonRef?.nativeElement) {
      this.incrementButtonRef.nativeElement.addEventListener('buttonClick', this.increment);
    }
    
    if (this.decrementButtonRef?.nativeElement) {
      this.decrementButtonRef.nativeElement.addEventListener('buttonClick', this.decrement);
    }
    
    if (this.resetButtonRef?.nativeElement) {
      this.resetButtonRef.nativeElement.addEventListener('buttonClick', this.reset);
    }
  }
  
  ngOnDestroy() {
    if (this.incrementButtonRef?.nativeElement) {
      this.incrementButtonRef.nativeElement.removeEventListener('buttonClick', this.increment);
    }
    
    if (this.decrementButtonRef?.nativeElement) {
      this.decrementButtonRef.nativeElement.removeEventListener('buttonClick', this.decrement);
    }
    
    if (this.resetButtonRef?.nativeElement) {
      this.resetButtonRef.nativeElement.removeEventListener('buttonClick', this.reset);
    }
  }
  
  increment = () => {
    this.store.dispatch(increment());
  }
  
  decrement = () => {
    this.store.dispatch(decrement());
  }
  
  reset = () => {
    this.store.dispatch(reset());
  }
}
```

## Handling Form State

### Reactive Forms with Modus Components

```typescript
@Component({
  selector: 'app-user-form',
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <div>
        <label for="name">Name:</label>
        <modus-text-input
          #nameInput
          placeholder="Enter name"
        ></modus-text-input>
      </div>
      <div>
        <label for="email">Email:</label>
        <modus-text-input
          #emailInput
          placeholder="Enter email"
        ></modus-text-input>
      </div>
      <modus-button #submitButton type="submit">Submit</modus-button>
    </form>
  `
})
export class UserFormComponent implements AfterViewInit, OnDestroy {
  @ViewChild('nameInput') nameInputRef!: ElementRef;
  @ViewChild('emailInput') emailInputRef!: ElementRef;
  @ViewChild('submitButton') submitButtonRef!: ElementRef;
  
  userForm = this.fb.group({
    name: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]]
  });
  
  constructor(private fb: FormBuilder) {}
  
  ngAfterViewInit() {
    // Sync the name input with form control
    if (this.nameInputRef?.nativeElement) {
      this.nameInputRef.nativeElement.value = this.userForm.get('name')?.value || '';
      
      this.nameInputRef.nativeElement.addEventListener('valueChange', this.onNameChange);
      
      this.userForm.get('name')?.valueChanges.subscribe(value => {
        if (this.nameInputRef.nativeElement.value !== value) {
          this.nameInputRef.nativeElement.value = value;
        }
      });
    }
    
    // Sync the email input with form control
    if (this.emailInputRef?.nativeElement) {
      this.emailInputRef.nativeElement.value = this.userForm.get('email')?.value || '';
      
      this.emailInputRef.nativeElement.addEventListener('valueChange', this.onEmailChange);
      
      this.userForm.get('email')?.valueChanges.subscribe(value => {
        if (this.emailInputRef.nativeElement.value !== value) {
          this.emailInputRef.nativeElement.value = value;
        }
      });
    }
    
    // Handle submit button
    if (this.submitButtonRef?.nativeElement) {
      this.submitButtonRef.nativeElement.addEventListener('buttonClick', this.onSubmit);
    }
  }
  
  ngOnDestroy() {
    if (this.nameInputRef?.nativeElement) {
      this.nameInputRef.nativeElement.removeEventListener('valueChange', this.onNameChange);
    }
    
    if (this.emailInputRef?.nativeElement) {
      this.emailInputRef.nativeElement.removeEventListener('valueChange', this.onEmailChange);
    }
    
    if (this.submitButtonRef?.nativeElement) {
      this.submitButtonRef.nativeElement.removeEventListener('buttonClick', this.onSubmit);
    }
  }
  
  onNameChange = (event: CustomEvent) => {
    this.userForm.get('name')?.setValue(event.detail);
  }
  
  onEmailChange = (event: CustomEvent) => {
    this.userForm.get('email')?.setValue(event.detail);
  }
  
  onSubmit = () => {
    if (this.userForm.valid) {
      console.log('Form submitted with:', this.userForm.value);
      // Send data to backend or perform other actions
    } else {
      // Mark fields as touched to show validation errors
      this.userForm.markAllAsTouched();
      
      // Update Modus components to show validation state
      if (this.nameInputRef?.nativeElement && this.userForm.get('name')?.invalid && this.userForm.get('name')?.touched) {
        this.nameInputRef.nativeElement.invalid = true;
        this.nameInputRef.nativeElement.errorText = 'Name is required';
      }
      
      if (this.emailInputRef?.nativeElement && this.userForm.get('email')?.invalid && this.userForm.get('email')?.touched) {
        this.emailInputRef.nativeElement.invalid = true;
        this.emailInputRef.nativeElement.errorText = 'Valid email is required';
      }
    }
  }
}
```

## Managing Navigation State

### Navigation Service with Modus SideNavigation

```typescript
// navigation.service.ts
@Injectable({
  providedIn: 'root'
})
export class NavigationService {
  private sidenavExpandedSubject = new BehaviorSubject<boolean>(false);
  sidenavExpanded$ = this.sidenavExpandedSubject.asObservable();
  
  private navItemsSubject = new BehaviorSubject<any[]>([
    { id: 'home', text: 'Home', icon: 'home', route: '/home' },
    { id: 'profile', text: 'Profile', icon: 'person', route: '/profile' },
    { id: 'settings', text: 'Settings', icon: 'settings', route: '/settings' }
  ]);
  navItems$ = this.navItemsSubject.asObservable();
  
  toggleSidenav() {
    this.sidenavExpandedSubject.next(!this.sidenavExpandedSubject.value);
  }
  
  updateNavItems(items: any[]) {
    this.navItemsSubject.next(items);
  }
}

// app.component.ts
@Component({
  selector: 'app-root',
  template: `
    <div class="app-container">
      <modus-navbar
        #modusNavbar
        appName="My Application"
        [showMainMenu]="true"
        logoUrl="https://modus.trimble.com/img/trimble-logo.svg"
      >
      </modus-navbar>
      <div class="content-container">
        <modus-side-navigation
          #modusSidenav
          [expanded]="sidenavExpanded$ | async"
          mode="push"
          targetContent="#main-content"
          style="height: calc(100vh - 56px);"
        >
        </modus-side-navigation>
        <main id="main-content">
          <router-outlet></router-outlet>
        </main>
      </div>
    </div>
  `,
  styles: [`
    .app-container {
      display: flex;
      flex-direction: column;
      height: 100vh;
    }
    .content-container {
      display: flex;
      flex: 1;
      position: relative;
    }
    #main-content {
      flex: 1;
      padding: 16px;
      overflow: auto;
    }
  `]
})
export class AppComponent implements AfterViewInit, OnDestroy {
  @ViewChild('modusNavbar') navbarRef!: ElementRef;
  @ViewChild('modusSidenav') sidenavRef!: ElementRef;
  
  sidenavExpanded$ = this.navigationService.sidenavExpanded$;
  
  constructor(private navigationService: NavigationService, private router: Router) {}
  
  ngAfterViewInit() {
    // Setup navbar event listener
    if (this.navbarRef?.nativeElement) {
      this.navbarRef.nativeElement.addEventListener('mainMenuClick', this.toggleSidenav);
    }
    
    // Initialize sidenav items
    if (this.sidenavRef?.nativeElement) {
      this.navigationService.navItems$.pipe(
        takeUntil(this.destroy$)
      ).subscribe(items => {
        if (this.sidenavRef.nativeElement.initialized) {
          this.sidenavRef.nativeElement.items = items;
        }
      });
      
      this.sidenavRef.nativeElement.addEventListener('itemClick', this.handleNavItemClick);
    }
  }
  
  private destroy$ = new Subject<void>();
  
  ngOnDestroy() {
    if (this.navbarRef?.nativeElement) {
      this.navbarRef.nativeElement.removeEventListener('mainMenuClick', this.toggleSidenav);
    }
    
    if (this.sidenavRef?.nativeElement) {
      this.sidenavRef.nativeElement.removeEventListener('itemClick', this.handleNavItemClick);
    }
    
    this.destroy$.next();
    this.destroy$.complete();
  }
  
  toggleSidenav = () => {
    this.navigationService.toggleSidenav();
  }
  
  handleNavItemClick = (event: CustomEvent) => {
    const route = event.detail.route;
    if (route) {
      this.router.navigate([route]);
    }
  }
}
```

## Best Practices for State Management

1. **Choose the Right Approach**
   - Use component state for simple, isolated components
   - Use services with RxJS for feature-level state management
   - Use NgRx or similar libraries for complex application state

2. **RxJS Best Practices**
   - Use BehaviorSubject for values that need an initial state
   - Always expose observables (not subjects) from services using `asObservable()`
   - Use the async pipe in templates when possible
   - Remember to unsubscribe from observables in ngOnDestroy

3. **State Updates with Modus Components**
   - Listen for Modus component events to update application state
   - Update Modus component properties when application state changes

4. **Performance Considerations**
   - Use OnPush change detection strategy
   - Avoid unnecessary state updates
   - Use memoized selectors when using NgRx
   - Consider using shareReplay for expensive computations

5. **Testing State Management**
   - Test services and NgRx effects/reducers in isolation
   - Mock Modus components in unit tests
   - Use integration tests for verifying component-state interactions
